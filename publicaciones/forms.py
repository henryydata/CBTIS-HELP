from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['contenido', 'archivo']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': '¿Qué estás pensando?'
            }),
            'archivo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*,video/*,application/pdf'
            })
        }

class PublicacionForm2(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['contenido', 'archivo', 'comunidad']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': '¿Qué estás pensando?'
            }),
            'archivo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*,video/*,application/pdf'
            }),
            'comunidad': forms.Select(attrs={
                'class': 'form-control'
            })
        }