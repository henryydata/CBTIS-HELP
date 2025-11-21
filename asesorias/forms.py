from django import forms 
from .models import Asesoria
import datetime
from django.core.exceptions import ValidationError

class AsesoriaForm(forms.ModelForm):
    class Meta:
        model = Asesoria
        validos = ('nombre', 'fecha', 'maestro', 'asignatura', 'escuela', 'categoria', 'cupo')
        fields = validos
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la asesoría'}),
            'fecha': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control', 'min': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')},
                format='%Y-%m-%dT%H:%M'
            ),
            'maestro': forms.Select(attrs={'class': 'form-select'}),
            'asignatura': forms.Select(attrs={'class': 'form-select'}),
            'escuela': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'cupo': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].input_formats = ('%Y-%m-%dT%H:%M',)