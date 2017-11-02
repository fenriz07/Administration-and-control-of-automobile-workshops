# encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class GlobalPermissionManager(models.Manager):
    def get_queryset(self):
        return super(GlobalPermissionManager, self).get_queryset().filter(content_type__model='global_permission')


class GlobalPermission(Permission):
    objects = GlobalPermissionManager()

    class Meta:
        proxy = True
        verbose_name = "global_permission"

    def save(self, *args, **kwargs):
        ct, created = ContentType.objects.get_or_create(model=self._meta.verbose_name, app_label=self._meta.app_label,)
        self.content_type = ct
        super(GlobalPermission, self).save(*args)


class Pais(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre


class Ciudad(models.Model):
    pais = models.ForeignKey(Pais)
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre