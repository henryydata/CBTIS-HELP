from django.db import models
from alumnos.models import Alumno
from categorias.models import Categoria

class Logro(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    nivel = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Logro {self.id} - {self.alumno}"
