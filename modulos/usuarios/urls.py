from django.conf.urls import url
from core.decorators import permiso_requerido
from .views import UsuariosListView, UsuariosCreateView, UsuariosEditView, UsuariosDeleteView

app_name = 'usuarios'
urlpatterns = [
    url(r'^$', permiso_requerido(UsuariosListView.as_view()), name="listar"),
    url(r'^(?P<pk>[0-9]+)/$', permiso_requerido(UsuariosEditView.as_view()), name="editar"),
    url(r'^registro/$', permiso_requerido(UsuariosCreateView.as_view()), name="registro"),
    url(r'^eliminar/(?P<pk>[0-9]+)/$', permiso_requerido(UsuariosDeleteView.as_view()), name="eliminar"),
    
]
