from django.db import models
from comunidades.models import Comunidad
from django.contrib.auth.models import User as Usuario

class Publicacion(models.Model):
    contenido = models.TextField()
    archivo = models.FileField(upload_to='comunidades/imagenes/', null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Publicación {self.id} - {self.autor}"
    
    def es_imagen(self):
        if self.archivo:
            ext = self.archivo.name.lower().split('.')[-1]
            return ext in ['jpg', 'jpeg', 'png', 'gif']
        return False
