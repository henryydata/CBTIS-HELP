from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto=models.ImageField(upload_to='perfil', null=True, blank=True)
    banner=models.ImageField(upload_to='banner', null=True, blank=True)
    biografia=models.TextField(max_length=50, null=True, blank=True)
    telefono=models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username