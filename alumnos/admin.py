from django.contrib import admin
from .models import Alumno, Semestre, Grupo

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido_paterno', 'apellido_materno', 'matricula', 'semestre', 'grupo')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'matricula')
    list_filter = ('semestre', 'grupo')
admin.site.register(Semestre)
admin.site.register(Grupo)

