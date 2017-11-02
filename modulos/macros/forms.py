# encoding: utf-8
from django import forms

class RegistroConsecutivoInspeccionForm(forms.Form):
    consecutivo_inspeccion = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-datos ancho', 'placeholder': u'Consecutivo para la inspección'}))

class RegistroMacroInspeccionForm(forms.Form):
    valor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-datos ancho', 'placeholder': u'Escriba un aspecto para la revisión visual'}))
