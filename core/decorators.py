from django.core.exceptions import PermissionDenied
from functools import wraps


def permiso_requerido(vista):
    @wraps(vista)
    def decorator(request, *args, **kwargs):
        nombre_vista = get_class_view(vista.func_name)
        if not nombre_vista in request.session['user_perms'] and not request.user.is_superuser:
            raise PermissionDenied
        return vista(request, *args, **kwargs)
    return decorator


def get_class_view(name):
    return {
        'IngresarVehiculosView': 'ingresar_vehiculo',
        'InspeccionListView': 'datos_basicos',
        'DatosBasicosView': 'datos_basicos',
        'CargaDocumentosView': 'carga_documentos',
        'InspeccionVisualView': 'inspeccion_visual',
        'FotografiasVehiculoView': 'fotografias_vehiculo',
        'CargaAnalisisView': 'carga_analisis',
        'CargarImprontasView': 'cargar_improntas',
        'UsuariosListView': 'usuarios',
        'UsuariosEditView': 'usuarios',
        'UsuariosCreateView': 'usuarios',
        'UsuariosDeleteView': 'usuarios',
        'BackupListView': 'backup',
        'SoporteView': 'soporte',
        'ReportesView': 'historial_reportes',
        'InspeccionReporteView': 'historial_reportes',
        'MostrarImprontaView': 'cargar_improntas'
    }.get(name)
