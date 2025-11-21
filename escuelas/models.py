from django.db import models
from django.utils.text import slugify

class Escuela(models.Model):
    nombre = models.CharField(max_length=5)
    plantel = models.CharField(max_length=5)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.plantel}"
    
    def save(self, *args, **kwargs):

        base_slug = slugify(f"{self.nombre}-{self.plantel}")
        slug = base_slug
        contador = 1

        while Escuela.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{contador}"
            contador += 1

        self.slug = slug
        super().save(*args, **kwargs)