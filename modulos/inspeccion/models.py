# encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import JSONField
from modulos.vehiculo.models import Vehiculo
from modulos.propietario.models import PropietarioVehiculo
from modulos.macros.models import Macros


class Inspeccion(models.Model):

    TIPO_SERVICIO = (
        ('particular', u'Particular'),
        ('publico', u'Público'),
        ('diplomatico', u'Diplomático'),
        ('oficial',u'Oficial'),
        ('especialRNMA',u'EspecialRNMA')
    )

    PASO = (
            ('carga_documentos', u'Carga de documentos'),
            ('inspeccion_visual', u'Inspeccion Visual'),
            ('fotografias_vehiculo', u'Fotografias'),
            ('carga_analisis', u'Carga Analisis')
        )

    propietario_vehiculo = models.ForeignKey(PropietarioVehiculo)
    tipo_servicio = models.CharField(max_length=100, default='particular', choices=TIPO_SERVICIO)
    kilometraje = models.CharField(max_length=100, null=True, blank=True)
    paso = models.CharField(max_length=100, null=True, blank=True, choices=PASO)
    finalizado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    numero_inspeccion = models.IntegerField()
    v_r_cliente = models.CharField(max_length=100,null=True, blank=True)
    v_r_empresa = models.CharField(max_length=100,null=True, blank=True)
    v_r_fasecolda = models.CharField(max_length=100,null=True, blank=True)
    v_r_accesorios = models.CharField(max_length=100,null=True, blank=True)

    def __unicode__(self):
        return self.tipo_servicio


class InspeccionDetalle(models.Model):
    VALOR_MACRO = (
        ('deficiente', u'Deficiente'),
        ('aceptable', u'Aceptable'),
        ('optimo', u'Óptimo'),
        ('no_aplica', u'No aplica'),
    )
    inspeccion = models.ForeignKey(Inspeccion)
    macro_value = JSONField(null=True, blank=True)
    observacion = models.TextField(null=True, blank=True)


class InspeccionFotografia(models.Model):
    inspeccion = models.ForeignKey(Inspeccion)
    img_superior_derecha = models.ImageField(upload_to="uploads/inspeccion", default='default/no-img.jpg')
    img_superior_izquierda = models.ImageField(upload_to="uploads/inspeccion", default='default/no-img.jpg')
    img_delantera = models.ImageField(upload_to="uploads/inspeccion", default='default/no-img.jpg')
    img_trasera = models.ImageField(upload_to="uploads/inspeccion", default='default/no-img.jpg')
    img_interior = models.ImageField(upload_to="uploads/inspeccion", default='default/no-img.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.inspeccion.propietario_vehiculo.propietario.nombre

class InspeccionImpronta(models.Model):
    inspeccion = models.ForeignKey(Inspeccion)
    impronta = models.FileField(upload_to='uploads/improntas')
    reated_at = models.DateTimeField(auto_now_add=True)
