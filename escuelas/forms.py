from django import forms
from .models import Escuela

class EscuelaForm(forms.ModelForm):
    class Meta:
        model = Escuela
        fields = ('nombre', 'plantel', 'telefono', 'direccion')

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. CBTIS 145',
                'style': 'border-radius:10px; border:2px solid #7a0c18;',
            }),
            'plantel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 145',
                'style': 'border-radius:10px; border:2px solid #7a0c18;',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 4421234567',
                'maxlength': '10',
                'style': 'border-radius:10px; border:2px solid #7a0c18;',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Calle, colonia, ciudad...',
                'style': 'border-radius:10px; border:2px solid #7a0c18;',
            }),
        }

        labels = {
            'nombre': 'Nombre de la escuela',
            'plantel': 'Número de plantel',
            'telefono': 'Teléfono de contacto',
            'direccion': 'Dirección completa',
        }
