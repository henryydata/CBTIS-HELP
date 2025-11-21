"""
URL configuration for cbtis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, "index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('alumnos/', include('alumnos.urls')),
    path('escuelas/', include('escuelas.urls')),
    path('maestros/', include('maestros.urls')),
    path('comunidades/', include('comunidades.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('publicaciones/', include('publicaciones.urls')),
    path('asesorias/', include('asesorias.urls')),
    path('asignaturas/', include('asignaturas.urls')),
    path('categorias/', include('categorias.urls')),
    path('especialidades/', include('especialidades.urls')),
    path('logros/', include('logros.urls')),
    path('sanciones/', include('sanciones.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
