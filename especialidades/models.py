from django.db import models
from escuelas.models import Escuela
from comunidades.models import Comunidad

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=250)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.especialidad
