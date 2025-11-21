from django.db import models
from django.contrib.auth.models import User
from escuelas.models import Escuela
from asignaturas.models import Asignatura

class Maestro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)

    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre