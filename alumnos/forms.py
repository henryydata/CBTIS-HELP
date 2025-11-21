from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'matricula',
            'escuela',
            'semestre',
            'grupo',
            'especialidad',
            'comunidad',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre(s)',
            }),
            'apellido_paterno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido paterno',
            }),
            'apellido_materno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido materno',
            }),
            'matricula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. CBTIS1452025',
            }),
            'escuela': forms.Select(attrs={
                'class': 'form-select',
            }),
            'semestre': forms.Select(attrs={
                'class': 'form-select',
            }),
            'grupo': forms.Select(attrs={
                'class': 'form-select',
            }),
            'especialidad': forms.Select(attrs={
                'class': 'form-select',
            }),
            'comunidad': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

        labels = {
            'nombre': 'Nombre(s)',
            'apellido_paterno': 'Apellido paterno',
            'apellido_materno': 'Apellido materno',
            'matricula': 'Matrícula',
            'escuela': 'Escuela',
            'semestre': 'Semestre',
            'grupo': 'Grupo',
            'especialidad': 'Especialidad',
            'comunidad': 'Comunidad',
        }