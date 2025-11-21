from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'tipo')
    search_fields = ('categoria',)
    list_filter = ('categoria',)
    ordering = ('categoria',)
