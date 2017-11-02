from django.conf.urls import url
from core.decorators import permiso_requerido

from .views import DatosBasicosView, CargaDocumentosView, CargaAnalisisView
from .views import InspeccionVisualView, FotografiasVehiculoView
from .views import InspeccionListView, CargarImprontasView, InspeccionReporteView

app_name = 'inspeccion'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', permiso_requerido(InspeccionReporteView.as_view()), name="reporte"),
    url(r'^$', permiso_requerido(InspeccionListView.as_view()), name="listar"),
    url(r'^datos-basicos/$', permiso_requerido(DatosBasicosView.as_view()), name="datos_basicos"),
    url(r'^carga-documentos/(?P<pk>[0-9]+)/$', permiso_requerido(CargaDocumentosView.as_view()), name="carga_documentos"),
    url(r'^inspeccion-visual/(?P<pk>[0-9]+)/$', permiso_requerido(InspeccionVisualView.as_view()), name="inspeccion_visual"),
    url(r'^fotografias-vehiculo/(?P<pk>[0-9]+)/$', permiso_requerido(FotografiasVehiculoView.as_view()), name="fotografias_vehiculo"),
    url(r'^carga-analisis/(?P<pk>[0-9]+)/$', permiso_requerido(CargaAnalisisView.as_view()), name="carga_analisis"),
    url(r'^cargar-improntas/(?P<pk>[0-9]+)/$', permiso_requerido(CargarImprontasView.as_view()), name="cargar_improntas"),
]
