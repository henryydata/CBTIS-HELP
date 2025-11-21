from django.db import models
from categorias.models import Categoria
from django.utils.text import slugify

class Comunidad(models.Model):
    comunidad = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=False, null=False)
    imagen = models.ImageField(upload_to='comunidades/', blank=True, null=True)
    descripcion = models.TextField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.comunidad)
            slug = base_slug
            n = 1
            while Comunidad.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comunidad

