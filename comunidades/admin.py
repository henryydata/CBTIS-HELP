from django.contrib import admin
from .models import Comunidad

@admin.register(Comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'comunidad','categoria')
    search_fields = ('comunidad',)


