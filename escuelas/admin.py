from django.contrib import admin
from .models import Escuela

@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre','plantel','telefono', 'direccion')
    search_fields = ('nombre',)
    list_filter = ('direccion',)
