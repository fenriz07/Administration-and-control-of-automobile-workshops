from django.contrib import admin

from modulos.inspeccion.models import Inspeccion, InspeccionFotografia, InspeccionDetalle

class InspeccionAdmin(admin.ModelAdmin):
    pass
    #list_display = ['p_vehiculo', 'created_at', 'updated_at']
    #list_filter = ['marca',]
    #search_fields = ['marca',]
admin.site.register(Inspeccion, InspeccionAdmin)


class FotografiasAdmin(admin.ModelAdmin):
    pass
    #list_display = ['inspeccion', 'img', 'angulo', 'created_at', 'updated_at']
    #list_filter = ['marca',]
    #search_fields = ['marca',]
admin.site.register(InspeccionFotografia, FotografiasAdmin)


class InspeccionDetalleAdmin(admin.ModelAdmin):
    pass
    #list_display = ['inspeccion', 'img', 'angulo', 'created_at', 'updated_at']
    #list_filter = ['marca',]
    #search_fields = ['marca',]
admin.site.register(InspeccionDetalle, InspeccionDetalleAdmin)