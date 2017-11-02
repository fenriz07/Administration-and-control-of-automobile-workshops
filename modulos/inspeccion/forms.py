# encoding: utf-8
from django import forms
from django_select2.forms import Select2Widget
from core.models import Ciudad
from modulos.macros.models import Macros
from modulos.propietario.models import Propietario
from modulos.vehiculo.models import Marca
from .models import Inspeccion, InspeccionDetalle


class DatosBasicosForm(forms.Form):

    TIPO_PROPIETARIO= (
        ('0', u'--- Seleccione una Opción ---'),
        ('1', u'Empresarial'),
        ('2', u'Personal'),
    )

    placa = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Escriba la placa del vehículo'}))
    placa_2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Escriba la placa del vehículo'}))
    numero_rombo = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-datos', 'placeholder': u'Número del rombo'}))
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.filter(pais__nombre__iexact='venezuela'), widget=Select2Widget(attrs={'class': 'form-datos' }))
    tipo_propietario = forms.ChoiceField(choices=TIPO_PROPIETARIO, widget=forms.Select(attrs={'class': 'form-datos','id':'mostrar'}))

    #Propietario Empresarial:
    razon_social = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Nombre del Propietario'}))
    nit = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-datos', 'placeholder': u'Número de Identificacion'}))
    nit_2 = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-datos', 'placeholder': u'Verifica NIT'}))

    #Propietatio Personal:
    nombres = forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Nombres del Propietario'}))
    apellidos = forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Apellidos del Propietario'}))
    tipo_identificacion = forms.ChoiceField(required=False,choices=Propietario.TIPO_DOCUMENTO,widget=forms.Select(attrs={'class': 'form-datos'}))
    cedula_ciudadania = forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Numero de Identificacion'}))
    edad = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'class': 'form-datos', 'placeholder': u'Edad del propietario'}))
    profesion_propietario = forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Profesion del Propietario'}))

    #ambas
    direccion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Direccion del Propietario'}))
    telefono_fijo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Telefono de Identificacion'}))
    telefono_celular = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Telefono de Personal'}))
    ciudad_2 = forms.ModelChoiceField(queryset=Ciudad.objects.filter(pais__nombre__iexact='venezuela'), widget=Select2Widget(attrs={'class': 'form-datos' }))

    #Datos Basico Vehiculo:
    marca_vehiculo = forms.ModelChoiceField(queryset=Marca.objects.all(), widget=Select2Widget(attrs={'class': 'form-datos' }))
    clase_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Clase del vehículo'}))
    tipo_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Tipo del vehículo'}))
    modelo_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Modelo del vehículo'}))
    carroceria_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Tipo de carroceria del vehículo'}))
    tipo_caja = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Tipo de caja del vehículo'}))
    nacionalidad_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Nacionalidad del vehículo'}))
    color_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Color del vehículo'}))
    tipo_pintura = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Tipo de pintura del vehículo'}))
    tipo_combustible = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Tipo de combustible del vehículo'}))
    cilindraje_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Cilindraje del vehículo'}))
    numero_motor_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'N° Motor'}))
    numero_serie_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'N° Serie'}))
    numero_chasis_vehiculo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'N° Chasis'}))
    servicio_vehiculo = forms.ChoiceField(choices=Inspeccion.TIPO_SERVICIO,widget=Select2Widget(attrs={'class': 'form-datos' }))
    kilometraje_vehiculo = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-datos', 'placeholder': u'Kilometraje'}))

    #Valores:
    v_r_cliente = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Valor del propietario'}))
    v_r_empresa = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Valor de la empresa'}))
    v_r_fasecolda = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Valor de Fasecolda'}))
    v_r_accesorios = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-datos', 'placeholder': u'Valor de los accesorios'}))

    def clean(self):

        cleaned_data = super(DatosBasicosForm, self).clean()

        tipo_propietario = cleaned_data.get("tipo_propietario")

        nombres =  cleaned_data.get("nombres")
        apellidos = cleaned_data.get("apellidos")
        tipo_identificacion = cleaned_data.get("tipo_identificacion")
        cedula_ciudadania = cleaned_data.get("cedula_ciudadania")
        edad =cleaned_data.get("edad")
        profesion_propietario = cleaned_data.get("profesion_propietario")

        razon_social = cleaned_data.get("razon_social")
        nit = cleaned_data.get("nit")
        nit_2 = cleaned_data.get("nit_2")


        if int(tipo_propietario) == 1:
            if len(razon_social) == 0 or len(str(nit)) == 0 or len(str(nit_2)) == 0:
                raise forms.ValidationError("Faltan campos en el tipo de propietatio empresarial")


        if int(tipo_propietario) == 2:
            if len(str(nombres)) == 0 or len(str(apellidos)) == 0 or len(str(tipo_identificacion)) == 0 or len(str(cedula_ciudadania)) == 0 or len(str(edad)) == 0 or len(str(profesion_propietario)) == 0:
                 raise forms.ValidationError("Faltan campos en el tipo de propietatio personal")


class CargaDocumentosForm(forms.Form):
    fotografia_delantera = forms.ImageField(widget=forms.ClearableFileInput(attrs={'id':'input_id'}))
    fotografia_trasera = forms.ImageField(widget=forms.ClearableFileInput(attrs={'id':'input_it'}))


class FotografiasVehiculoForm(forms.Form):
    fotografia_superior_derecha = forms.CharField(widget=forms.TextInput(attrs={'id':'data_fotografia_superior_derecha','type':'hidden'}))
    fotografia_superior_izquierda = forms.CharField(widget=forms.TextInput(attrs={'id':'data_fotografia_superior_izquierda','type':'hidden'}))
    fotografia_delantera = forms.CharField(widget=forms.TextInput(attrs={'id':'data_fotografia_delantera','type':'hidden'}))
    fotografia_trasera = forms.CharField(widget=forms.TextInput(attrs={'id':'data_fotografia_trasera','type':'hidden'}))
    fotografia_interior = forms.CharField(widget=forms.TextInput(attrs={'id':'data_fotografia_interior','type':'hidden'}))


class CargaAnalisisForm(forms.Form):
    analisis = forms.FileField()

    def clean_analisis(self):
        analisis_a = self.cleaned_data["analisis"]
        if analisis_a.content_type != "text/plain":
            raise forms.ValidationError(u"Error: el tipo de archivo debe ser (txt).")
        return analisis_a


class CargaImprontaForm(forms.Form):
    impronta = forms.FileField()

    def clean_impronta(self):
        impronta = self.cleaned_data["impronta"]
        if impronta.content_type != "application/pdf":
            raise forms.ValidationError(u"Error: el tipo de archivo debe ser (PDF).")
        return impronta
