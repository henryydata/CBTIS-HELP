from django.db import models
from alumnos.models import Alumno

class Sancion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"Sanción: {self.motivo} - {self.alumno}"
