# encoding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import uuid

class Usuario(models.Model):
    TIPO_DOCUMENTO = (
        ('documento_nacional', u'Cédula de ciudadanía'),
        ('documento_extranjero', u'Cédula de extranjería'), 
        ('nit', u'NIT'), 
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=100, choices=TIPO_DOCUMENTO, null=True, blank=True)
    numero_documento = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    telefono_emergencia = models.CharField(max_length=100, null=True, blank=True)
    fotografia = models.ImageField(upload_to='usuario', default='default/no-img.jpg')
    
