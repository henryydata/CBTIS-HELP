from django import forms 
from .models import Comunidad

class ComunidadForm(forms.ModelForm):
    class Meta:
        model = Comunidad
        validos = ('comunidad', 'categoria','imagen', 'descripcion')
        fields = validos