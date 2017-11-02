from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from core.decorators import permiso_requerido

from core.views import LoginView, LogoutView
from core.views import DashboardView, ReportesView
from core.views import BackupListView, BackupRestoreView, BackupDeleteView
from core.views import _404, _403, _500
from core.views import MostrarImprontaView



urlpatterns = [

    url(r'^$', DashboardView.as_view(), name='inicio'),
    url(r"^login/$", LoginView.as_view(), name="login"),
    url(r"^logout/$", LogoutView.as_view(), name="logout"),

    url(r'^reportes/$', permiso_requerido(ReportesView.as_view()), name='reportes'),
    url(r'^backup/$', permiso_requerido(BackupListView.as_view()), name='backup'),
    url(r'^backup/restore/(?P<backup>.+)/$', permiso_requerido(BackupRestoreView.as_view()), name='backup_restore'),
    url(r'^backup/delete/(?P<backup>.+)/$', permiso_requerido(BackupDeleteView.as_view()), name='backup_delete'),
    #url(r'^mostrar_impronta/(?P<pk>[0-9]+)/$', permiso_requerido(MostrarImprontaView.as_view()), name="mostrar_impronta"),
    url(r'^mostrar_impronta/(?P<pk>[0-9]+)/$', permiso_requerido(MostrarImprontaView.as_view()), name="mostrar_impronta"),


    url(r'^404$', _404, name="not_found"),
    url(r'^403$', _403, name="permission_denied"),
    url(r'^500$', _500, name="server_error"),

    url(r"^usuarios/", include("modulos.usuarios.urls")),
    url(r"^macros/", include("modulos.macros.urls")),
    url(r"^vehiculos/", include("modulos.inspeccion.urls")),

    url(r'^admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
