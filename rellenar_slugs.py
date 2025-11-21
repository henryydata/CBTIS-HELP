from comunidades.models import Comunidad
from django.utils.text import slugify

for c in Comunidad.objects.all():
    if not c.slug:
        base_slug = slugify(c.comunidad)
        slug = base_slug
        n = 1
        while Comunidad.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{n}"
            n += 1
        c.slug = slug
        c.save()
        print(f"Slug generado para {c.comunidad}: {c.slug}")
