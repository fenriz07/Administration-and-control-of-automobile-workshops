# encoding: utf-8
from __future__ import unicode_literals
from django.db import models

from core.models import Ciudad
from modulos.vehiculo.models import Vehiculo,Color


class Propietario(models.Model):

    TIPO_PROPIETARIO = (
        ('personal', u'Personal'),
        ('empresarial', u'Empresarial'),
    )

    TIPO_DOCUMENTO = (
        ('documento_nacional', u'Cédula de ciudadanía'),
        ('documento_extranjero', u'Cédula de extranjería'),
        ('pasaporte', u'Pasaporte'),
        ('nit',u'NIT'),
        ('nin',u'NIN'),
        ('tarjeta_identidad',u'Tarjeta de identidad'),
        ('registro_civil',u'Registro civil'),
        ('carnet_diplomatico',u'Carnet diplomatico'),
        ('ti2',u'TI2'),
    )

    tipo_propietario = models.CharField(max_length=100, default='personal', choices=TIPO_PROPIETARIO)
    tipo_documento = models.CharField(max_length=100, choices=TIPO_DOCUMENTO, null=True, blank=True)
    numero_documento = models.CharField(max_length=100, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200, null=True, blank=True)
    edad = models.CharField(max_length=3, null=True, blank=True)
    telefono_fijo = models.CharField(max_length=100, null=True, blank=True)
    telefono_celular = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    profesion = models.CharField(max_length=250, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Licencia(models.Model):
    propietario = models.ForeignKey(Propietario)
    imagen_delantera = models.ImageField(upload_to="uploads/licencia", default='default/no-img.jpg')
    imagen_trasera = models.ImageField(upload_to="uploads/licencia", default='default/no-img.jpg')

    def __unicode__(self):
        return self.propietario.nombre


class PropietarioVehiculo(models.Model):
    propietario = models.ForeignKey(Propietario)
    vehiculo = models.ForeignKey(Vehiculo)
    color = models.ForeignKey(Color)
    tipo_pintura = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    numero_chasis = models.CharField(max_length=100)
    numero_motor = models.CharField(max_length=100)
    placa = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True)
    rombo = models.CharField(max_length=100)

    def __unicode__(self):
        return u'{} {}'.format(self.propietario.nombre, self.vehiculo.modelo.nombre)
