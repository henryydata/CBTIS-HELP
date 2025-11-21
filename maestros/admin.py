from django.contrib import admin
from .models import Maestro

@admin.register(Maestro)
class MaestroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno')
