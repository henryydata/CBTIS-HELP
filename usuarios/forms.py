from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from alumnos.models import Alumno
from maestros.models import Maestro

class RegistroForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password']

class CrearCuentaAlumnoForm(UserCreationForm):
    matricula = forms.CharField(max_length=20)
    first_name = forms.CharField(label="Nombre", max_length=100)
    last_name = forms.CharField(label="Apellido", max_length=100)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "matricula"]

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            placeholders = {
                "username": "Usuario",
                "email": "alumno@ejemplo.com",
                "first_name": "Nombre(s)",
                "last_name": "Apellido(s)",
                "password1": "Ingresa una contraseña",
                "password2": "Confirma tu contraseña",
                "matricula": "Ingresa tu matrícula",
            }
            for name, field in self.fields.items():
                field.widget.attrs.update({
                    "class": "form-control mb-2",
                    "placeholder": placeholders.get(name, "")
                })


class CrearCuentaMaestroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido_paterno = forms.CharField(max_length=100, label="Apellido paterno")
    apellido_materno = forms.CharField(max_length=100, label="Apellido materno")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "nombre", "apellido_paterno", "apellido_materno"]

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido_paterno = cleaned_data.get("apellido_paterno")
        apellido_materno = cleaned_data.get("apellido_materno")
        if not Maestro.objects.filter(
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno
        ).exists():
            raise forms.ValidationError("⚠️ No se encontró este maestro en la base de datos.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["nombre"]
        user.last_name = f"{self.cleaned_data['apellido_paterno']} {self.cleaned_data['apellido_materno']}"
        if commit:
            user.save()
        return user
