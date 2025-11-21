from django.db import models
from django.contrib.auth.models import AbstractUser

class Escuela(models.Model):
    nombre = models.CharField(max_length=200)
    plantel = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Semestre(models.Model):
    semestre = models.CharField(max_length=150)

    def __str__(self):
        return self.semestre


class Escuela(models.Model):
    nombre = models.CharField(max_length=200)
    plantel = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    grupo = models.CharField(max_length=150)

    def __str__(self):
        return self.grupo


class Categoria(models.Model):
    categoria = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.categoria


class Especialidad(models.Model):
    especialidad = models.CharField(max_length=250)

    def __str__(self):
        return self.especialidad


class Comunidad(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comunidad {self.id} - {self.especialidad}"


class Asignatura(models.Model):
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"Asignatura {self.id} ({self.escuela})"


# =======================
# ALUMNOS Y MAESTROS
# =======================

class Alumno(models.Model):
    no_control = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    semestre = models.ForeignKey(Semestre, on_delete=models.PROTECT)
    escuela = models.ForeignKey(Escuela, on_delete=models.PROTECT)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Maestro(models.Model):
    nombre = models.CharField(max_length=200)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    asignaturas = models.ManyToManyField(Asignatura, blank=True)

    def __str__(self):
        return self.nombre

class Sancion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"Sanción: {self.motivo} - {self.alumno}"


class Asesoria(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"Asesoría {self.id} - {self.alumno} con {self.maestro}"


class Logro(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    nivel = models.CharField(max_length=100, null=True, blank=True)  # Ej. Oro, Plata, Bronce

    def __str__(self):
        return f"Logro {self.id} - {self.alumno}"