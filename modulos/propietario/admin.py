from django.contrib import admin

from modulos.propietario.models import Propietario, Licencia, PropietarioVehiculo

class PropietarioAdmin(admin.ModelAdmin):
    pass
    #list_display = ['documento_identidad', 'nombre', 'apellido', 'sexo', 'telefono', 'email']
    #list_filter = ['sexo',]
    #search_fields = ['documento_identidad', 'nombre', 'apellido', 'email']
admin.site.register(Propietario, PropietarioAdmin)


class PropietarioVehiculoAdmin(admin.ModelAdmin):
    pass
    #list_display = ['propietario', 'vehiculo', 'color', 'placa']
    #list_filter = ['color',]
    #search_fields = ['color', 'placa']
admin.site.register(PropietarioVehiculo, PropietarioVehiculoAdmin)


class LicenciaAdmin(admin.ModelAdmin):
    pass
    #list_display = ['propietario', 'numero', 'fecha_expedicion', 'fecha_vencimiento']
    #list_filter = ['numero',]
    #search_fields = ['numero',]
admin.site.register(Licencia, LicenciaAdmin)