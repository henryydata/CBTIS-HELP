from django.contrib import admin
from .models import Especialidad

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display=('id','especialidad','escuela','comunidad')
    list_filter=('especialidad',)
