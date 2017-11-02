from django.contrib import admin

from modulos.vehiculo.models import Marca, Modelo, Vehiculo

class MarcaAdmin(admin.ModelAdmin):
    pass
    #list_display = ['marca',]
    #list_filter = ['marca',]
    #search_fields = ['marca',]
admin.site.register(Marca, MarcaAdmin)


class ModeloAdmin(admin.ModelAdmin):
    pass
    #ist_display = ['marca', 'modelo']
    #list_filter = ['marca__marca', ]
    #search_fields = ['marca__marca', 'modelo']

admin.site.register(Modelo, ModeloAdmin)


class VehiculoAdmin(admin.ModelAdmin):
    pass
    #list_display = ['related_marca', 'modelo', 'ano', 'tipo', 'motor', 'cilindros']
    #list_filter = ['modelo__marca__marca', 'modelo__modelo', 'tipo']
    #search_fields = ['modelo__marca', 'tipo']

    #def related_marca(self, obj):
    #    return obj.modelo.marca.marca
    #related_marca.short_description = 'Marca'

admin.site.register(Vehiculo, VehiculoAdmin)