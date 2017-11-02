# encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify

class ConsecutivoInspeccion(models.Model):
    codigo_inspeccion = models.IntegerField()


class Macros(models.Model):
    TIPO_INSPECCION = (
        ('motor', u'Motor'),
        ('exterior', u'Exterior'),
        ('interior', u'Interior'),
        ('parte_baja', u'Parte Baja'),
    )
    tipo = models.CharField(max_length=100, choices=TIPO_INSPECCION) # motor
    nombre = models.CharField(max_length=200) # nivel de aceite, compresion, etc
    nombre_slug = models.SlugField(null=True, blank=True)


    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)[:50]
        return super(Macros, self).save(*args, **kwargs)
