# encoding: utf-8
from django.contrib.auth.models import Permission
from django import forms
from django.contrib.auth.models import User
from modulos.usuarios.models import Usuario


class RegistroForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ('user',)

    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Escriba el nombre'}))
    apellido = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Escriba el apellido'}))
    tipo_documento = forms.ChoiceField(choices=Usuario.TIPO_DOCUMENTO, widget=forms.Select(attrs={'class': 'form-control'}))
    numero_documento = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Escriba el número de documento'}))
    direccion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Escriba la dirección de residencia'}))
    telefono = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Escriba el teléfono'}))
    telefono_emergencia = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Escriba un teléfono para casos de emergencia'}))
    fotografia = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': u'Escriba el correo electrónico'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'Escriba la contraseña'}))
    permisos = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=Permission.objects.filter(content_type__model='globalpermission').order_by('id'),
    )

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)

        # Si el formulario se esta editando, no validamos fotografia ni password
        if self.instance.id:
            self.initial['nombre'] = self.instance.user.first_name
            self.initial['apellido'] = self.instance.user.last_name
            self.initial['email'] = self.instance.user.email
            self.initial['permisos'] = self.instance.user.user_permissions.all()
            self.fields['email'].disabled = True
            self.fields['fotografia'].required = False
            self.fields['password'].required = False


    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        # Si el formulario no se esta editando, validamos el usuario
        if not self.instance.id:
            user = User.objects.filter(username=email).first()
            if user:
                raise forms.ValidationError(u"Este email ya se encuentra registrado.")
        return email
