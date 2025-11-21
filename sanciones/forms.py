from django import forms
from .models import Sancion

class SancionForm(forms.ModelForm):
    class Meta:
        model=Sancion
        fields='__all__'
        widgets = {
            'motivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motivo de la sancion'}),
            'fecha_hora': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'alumno': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_hora'].input_formats = ('%Y-%m-%dT%H:%M',)