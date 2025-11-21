from django.db import models
from categorias.models import Categoria

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'
