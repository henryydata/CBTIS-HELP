from django.db import models
from maestros.models import Maestro
from asignaturas.models import Asignatura
from categorias.models import Categoria
from escuelas.models import Escuela
from alumnos.models import Alumno

class Asesoria(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateTimeField()

    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cupo = models.PositiveIntegerField(default=10)
    inscritos = models.ManyToManyField(Alumno, blank=True)

    @property
    def cupos_restantes(self):
        inscritos_activos = self.inscripcionasesoria_set.filter(estado=True).count()
        return self.cupo - inscritos_activos

class InscripcionAsesoria(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asesoria = models.ForeignKey(Asesoria, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)

    class Meta:
        unique_together = ('alumno', 'asesoria')

