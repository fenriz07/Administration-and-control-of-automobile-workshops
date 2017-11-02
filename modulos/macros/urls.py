from django.conf.urls import url
from core.decorators import permiso_requerido
from .views import *

app_name = 'macros'
urlpatterns = [

    url(r"^consecutivo_inspeccion/$", permiso_requerido(ConsecutivoInspeccionView.as_view()), name="consecutivo_inspeccion"),
    url(r"^inspeccion_exterior/$", permiso_requerido(InspecionExteriorView.as_view()), name="inspeccion_exterior"),
    url(r"^inspeccion_interior/$", permiso_requerido(InspeccionInteriorView.as_view()), name="inspeccion_interior"),
    url(r"^inspeccion_motor/$", permiso_requerido(InspeccionMotorView.as_view()), name="inspeccion_motor"),
    url(r"^inspeccion_parte_baja/$", permiso_requerido(InspeccionParteBajaView.as_view()), name="inspeccion_parte_baja"),
    url(r"^borrar_macro/(?P<id_macro>\d+)/$", permiso_requerido(BorrarMacroView.as_view()), name="borrar_macro"),
]
