from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def siguiente(context):
    msg = 'SIGUIENTE'
    actual = context.request.path.split('/')[2]
    siguiente = next_opt(actual)
    if (not siguiente[1] in context.request.session['user_perms'] and not context.request.user.is_superuser) or (siguiente[1] == 'terminar'):
        msg = 'TERMINAR'
    return msg


def next_opt(actual):
    return {
        'datos-basicos': 'carga_documentos',
        'carga-documentos': 'inspeccion_visual',
        'inspeccion-visual': 'fotografias_vehiculo',
        'fotografias-vehiculo': 'carga_analisis',
    }.get(actual, 'terminar')


"""
def next_opt(actual):
    return {
        'datos-basicos': [reverse('inspeccion:carga_documentos'), 'carga_documentos'],
        'carga-documentos': [reverse('inspeccion:inspeccion_visual'), 'inspeccion_visual'],
        'inspeccion-visual': [reverse('inspeccion:fotografias_vehiculo'), 'fotografias_vehiculo'],
        'fotografias-vehiculo': [reverse('inspeccion:carga_analisis'), 'carga_analisis'],
    }.get(actual, [reverse('inspeccion:listar'), 'terminar'])


@register.simple_tag(takes_context=True)
def regresar(context, inspeccion_id):
    import ipdb; ipdb.set_trace()
    actual = context.request.path.split('/')[2]
    return prev_opt(actual)


def prev_opt(actual):
    return {
        'carga-documentos': reverse('inspeccion:datos_basicos'),
        'inspeccion-visual': reverse('inspeccion:carga_documentos'),
        'fotografias-vehiculo': reverse('inspeccion:inspeccion_visual'),
        'carga-analisis': reverse('inspeccion:fotografias_vehiculo'),
    }.get(actual, reverse('inspeccion:listar'))
"""