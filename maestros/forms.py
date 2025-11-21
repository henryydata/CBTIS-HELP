from django import forms
from .models import Maestro

class MaestroForm(forms.ModelForm):
    class Meta:
        validos=('nombre','apellido_paterno','apellido_materno','asignatura','escuela')
        model=Maestro
        fields=validos