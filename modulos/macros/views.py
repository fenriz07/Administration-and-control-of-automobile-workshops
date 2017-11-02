# encoding: utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, RedirectView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django import http
from .forms import *
from .models import *
from django.shortcuts import render, render_to_response, redirect
from core.views import BaseWebMixin


class ConsecutivoInspeccionView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        CI = ConsecutivoInspeccion.objects.last()
        
        if hasattr(CI, 'codigo_inspeccion'):
            context = {'consecutivo_inspeccion': CI.codigo_inspeccion}
        else:
            context = {'form': RegistroConsecutivoInspeccionForm}
        return render(request, 'macros/consecutivo-inspeccion.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistroConsecutivoInspeccionForm(request.POST)

        if form.is_valid():
            consecutivo_inspeccion = form.cleaned_data['consecutivo_inspeccion']
            CI = ConsecutivoInspeccion.objects.create(
                codigo_inspeccion = consecutivo_inspeccion,
            )

            messages.success(request, u'Código consecutivo de inspección agregado')
            return redirect(request.META['HTTP_REFERER'])

        context = {'form': form}
        return render(request, 'macros/consecutivo-inspeccion.html', context)


class InspeccionMotorView(BaseWebMixin):
    tipo = "motor"

    def get(self, request, *args, **kwargs):
        valores_macro = Macros.objects.filter(tipo=self.tipo)
        context = {'form':RegistroMacroInspeccionForm,'valores_macro':valores_macro,'tipo':self.tipo}
        return render(request, 'macros/inspeccion-motor.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistroMacroInspeccionForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            macro = Macros.objects.create(
                tipo = self.tipo,
                nombre = valor,
            )
        messages.success(request, u'Aspecto del motor agregado')
        return redirect('/macros/inspeccion_motor')


class InspecionExteriorView(BaseWebMixin):
    tipo = "exterior"

    def get(self, request, *args, **kwargs):
        valores_macro = Macros.objects.filter(tipo=self.tipo)
        context = {'form':RegistroMacroInspeccionForm,'valores_macro':valores_macro,'tipo':self.tipo}
        return render(request, 'macros/inspeccion-exterior.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistroMacroInspeccionForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            macro = Macros.objects.create(
                tipo = self.tipo,
                nombre = valor,
            )
        messages.success(request, u'Aspecto exterior agregado')
        return redirect('/macros/inspeccion_exterior')


class InspeccionInteriorView(BaseWebMixin):
    tipo = "interior"
    def get(self, request, *args, **kwargs):
        valores_macro = Macros.objects.filter(tipo=self.tipo)
        context = {'form':RegistroMacroInspeccionForm,'valores_macro':valores_macro,'tipo':self.tipo}
        return render(request, 'macros/inspeccion-interior.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistroMacroInspeccionForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            macro = Macros.objects.create(
                tipo = self.tipo,
                nombre = valor,
            )
        messages.success(request, u'Aspecto interior agregado')
        return redirect('/macros/inspeccion_interior')


class InspeccionParteBajaView(BaseWebMixin):
    tipo = "parte_baja"
    def get(self, request, *args, **kwargs):
        valores_macro = Macros.objects.filter(tipo=self.tipo)
        context = {'form':RegistroMacroInspeccionForm, 'valores_macro':valores_macro, 'tipo':self.tipo}
        return render(request, 'macros/inspeccion-parte-baja.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistroMacroInspeccionForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            macro = Macros.objects.create(
                tipo = self.tipo,
                nombre = valor,
            )
        messages.success(request, u'Aspecto parte baja agregado')
        return redirect('/macros/inspeccion_parte_baja')


class BorrarMacroView(BaseWebMixin):
    def get(self, request, *args, **kwargs):
        macro = kwargs['id_macro']
        Macros.objects.filter(id=macro).delete()
        return redirect(request.META['HTTP_REFERER'])
