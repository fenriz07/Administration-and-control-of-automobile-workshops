# encoding: utf-8
import re
import os
from datetime import datetime
from threading import Thread

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, RedirectView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django import http
from django.shortcuts import render, redirect, Http404
from django.core import management
from django.conf import settings
from django_cron import CronJobBase, Schedule


from modulos.inspeccion.models import Inspeccion, InspeccionImpronta


class BaseWebMixin(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class DashboardView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        archivos = os.listdir(settings.DBBACKUP_STORAGE_OPTIONS.get('location'))
        archivos.sort(key=natural_sort_key)
        last_backup = re.search(r'(\d+-\d+-\d+)', archivos[-1])
        context = {
            'inspecciones': Inspeccion.objects.all().order_by('-id')[:10],
            'total_inspecciones': Inspeccion.objects.count(),
            'last_backup': last_backup.group(0)
        }
        return render(request, 'dashboard/index.html', context)


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            request.session['user_perms'] = [x.codename for x in user.user_permissions.all()]
            return redirect(reverse('inicio'))
        return render(request, 'login.html', {'error': 'Correo o clave incorrecta'})


class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        try:
            logout(request)
            del request.session['user_perms']
        except:
            pass
        return redirect(reverse('login'))


class ReportesView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        placa = request.GET.get('placa', False)
        inspecciones = Inspeccion.objects.all().order_by('-id')

        if placa:
            inspecciones = inspecciones.filter(propietario_vehiculo__placa__icontains=placa)

        paginator = Paginator(inspecciones, 10)
        page = request.GET.get('page')
        try:
            inspecciones = paginator.page(page)
        except PageNotAnInteger:
            inspecciones = paginator.page(1)
        except EmptyPage:
            inspecciones = paginator.page(paginator.num_pages)
        return render(request, 'reportes/historial.html', {'inspecciones': inspecciones})


class MostrarImprontaView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        inspeccion_impronta = InspeccionImpronta.objects.filter(inspeccion_id=kwargs.get('pk')).values()
        if inspeccion_impronta:
            ruta_archivo = inspeccion_impronta[0]['impronta']
            archivo_pdf = open(settings.MEDIA_ROOT+'/'+ruta_archivo,'r')
            response = http.HttpResponse(archivo_pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="impronta.pdf"'
            return response
        
        messages.warning(request,u'Impronta no cargada')
        return redirect(request.META['HTTP_REFERER'])


class BackupListView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        archivos = os.listdir(settings.DBBACKUP_STORAGE_OPTIONS.get('location'))
        archivos.sort(key=natural_sort_key)
        return render(request, 'backup/backup.html', {'respaldos': archivos})

    def post(self, request, *args, **kwargs):
        backup()
        messages.success(request, u'Se está realizando el respaldo de la base de datos, en unos minutos estará disponible.')
        return redirect(reverse('backup'))


class BackupRestoreView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        filename = kwargs.get('backup')
        path = settings.DBBACKUP_STORAGE_OPTIONS.get('location')
        archivo = path + '/' + filename
        try:
            size = os.path.getsize(archivo)
        except:
            raise Http404()
        return render(request, 'backup/restaurar.html', {'archivo': size})

    def post(self, request, *args, **kwargs):
        filename = kwargs.get('backup')
        path = settings.DBBACKUP_STORAGE_OPTIONS.get('location')
        archivo = path + '/' + filename
        restore(archivo)
        return redirect(reverse('backup'))


class BackupDeleteView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        filename = kwargs.get('backup')
        path = settings.DBBACKUP_STORAGE_OPTIONS.get('location')
        archivo = path + '/' + filename
        try:
            size = os.path.getsize(archivo)
        except:
            raise Http404()
        return render(request, 'backup/eliminar.html', {'archivo': size})

    def post(self, request, *args, **kwargs):
        filename = kwargs.get('backup')
        path = settings.DBBACKUP_STORAGE_OPTIONS.get('location')
        archivo = path + '/' + filename
        drop(archivo)
        messages.warning(request, u'Se ha eliminado el respaldo %s' % (filename,))
        return redirect(reverse('backup'))


class BackupCron(CronJobBase):
    RUN_AT_TIMES = ['23:00', ]
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'core.BackupCron'

    def do(self):
        backup()


def _404(request):
    return render(request, '404.html')


def _403(request):
    return render(request, '403.html')


def _500(request):
    return render(request, '500.html')


def natural_sort_key(s):
    _nsre = re.compile('([0-9]+)')
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]


def postpone(function):
    def decorator(*args, **kwargs):
        t = Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator


@postpone
def backup():
    archivos = os.listdir(settings.DBBACKUP_STORAGE_OPTIONS.get('location'))
    if len(archivos) > 2:
        archivos.sort(key=natural_sort_key)
        path = settings.DBBACKUP_STORAGE_OPTIONS.get('location')
        archivo = path + '/' + archivos[0]
        try:
            os.remove(archivo)
        except:
            pass
    management.call_command('dbbackup', output_filename=datetime.now().strftime('%Y-%m-%d__%H:%M:%S')+'.psql')


@postpone
def restore(archivo):
    management.call_command('dbrestore', '--noinput', input_path=archivo)


@postpone
def drop(archivo):
    try:
        os.remove(archivo)
    except:
        pass
