from django.contrib import admin
from .models import Asignatura
# Register your models here.
@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display=('nombre','categoria')
    