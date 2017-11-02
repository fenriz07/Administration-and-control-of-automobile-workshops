# encoding: utf-8
from __future__ import unicode_literals
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Modelo(models.Model):
    marca = models.ForeignKey(Marca)
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class ClaseVehiculo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class TipoCarroceria(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class NacionalidadVehiculo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Vehiculo(models.Model):
    modelo = models.ForeignKey(Modelo)
    ano = models.PositiveIntegerField()
    clase = models.ForeignKey(ClaseVehiculo)
    tipo = models.CharField(max_length=100)
    carroceria = models.ForeignKey(TipoCarroceria)
    tipo_caja = models.CharField(max_length=100)
    tipo_combustible = models.ForeignKey(TipoCombustible)
    cilindraje = models.CharField(max_length=20)
    nacionalidad = models.ForeignKey(NacionalidadVehiculo)

    def __unicode__(self):
        return '{}, {}'.format(self.modelo, self.ano)
