from django.db import models
from django.contrib.auth.models import User
from escuelas.models import Escuela
from comunidades.models import Comunidad
from especialidades.models import Especialidad

class Semestre(models.Model):
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.numero}"


class Grupo(models.Model):
    nombre = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)

    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True, blank=True)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"
