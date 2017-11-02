# encoding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Permission

from core.views import BaseWebMixin
from .forms import RegistroForm
from .models import Usuario


class UsuariosListView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all().order_by('-id')
        paginator = Paginator(usuarios, 10)
        page = request.GET.get('page')
        try:
            usuarios = paginator.page(page)
        except PageNotAnInteger:
            usuarios = paginator.page(1)
        except EmptyPage:
            usuarios = paginator.page(paginator.num_pages)
        return render(request, 'usuarios/listar.html', {'usuarios':usuarios})


class UsuariosEditView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=kwargs.get('pk'))
        context = {'form': RegistroForm(instance=usuario)}
        return render(request, 'usuarios/editar.html', context)

    def post(self, request, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=kwargs.get('pk'))
        form = RegistroForm(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            data = form.cleaned_data
            usuario.user.first_name = data['nombre']
            usuario.user.last_name = data['apellido']
            if data['password'] != '':
                usuario.user.set_password(data['password'])
            
            usuario.user.save()
            form.save()

            # Agrega nuevos permisos
            for permiso in data['permisos']:
                usuario.user.user_permissions.add(permiso)

            # elimina permisos
            drop_perms = [x for x in usuario.user.user_permissions.all() if x not in set(data['permisos'])]
            for permiso in drop_perms:
                usuario.user.user_permissions.remove(permiso)
            
            messages.success(request, 'El usuario se actualizó correctamente.')
            return redirect(reverse('usuarios:editar', args=(usuario.id,)))
        
        return render(request, 'usuarios/editar.html', {'form': form})
        

class UsuariosCreateView(BaseWebMixin):
   
    def get(self, request, *args, **kwargs):
        context = {'form': RegistroForm}
        return render(request, 'usuarios/crear.html', context)

    def post(self, request, *args, **kwargs):

        form = RegistroForm(request.POST, request.FILES)
      
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['email'], 
                email=data['email'], 
                password=data['password'],
                first_name=data['nombre'], 
                last_name=data['apellido'], 
                )

            for permiso in data['permisos']:
                user.user_permissions.add(permiso)

            usuario = Usuario.objects.create(
                user = user,
                tipo_documento = data['tipo_documento'],
                numero_documento= data['numero_documento'],
                direccion = data['direccion'],
                telefono = data['telefono'],
                telefono_emergencia = data['telefono_emergencia'],
                fotografia = data['fotografia'],
                )

            messages.success(request, u'El usuario se creó correctamente.')
            return redirect(reverse('usuarios:registro'))

        return render(request, 'usuarios/crear.html', {'form': form})
        

class UsuariosDeleteView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=kwargs.get('pk'))
        return render(request, 'usuarios/eliminar.html', {'usuario':usuario})

    def post(self, request, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=kwargs.get('pk'))
        usuario.delete()
        messages.success(request, u'El usuario se eliminó correctamente.')
        return redirect(reverse('usuarios:listar'))