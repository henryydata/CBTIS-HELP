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
from django.conf.urls import handler404, handler500, handler403, handler400

def home(request):
    return render(request, "index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('dashboard/', views.dashboard, name='dashboard'),
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

def custom_404(request, exception):
    return render(request, "404.html", status=404)

def custom_500(request):
    return render(request, "500.html", status=500)

def custom_403(request, exception):
    return render(request, "403.html", status=403)

def custom_400(request, exception):
    return render(request, "400.html", status=400)

handler404 = 'cbtis.urls.custom_404'
handler500 = 'cbtis.urls.custom_500' 
handler403 = 'cbtis.urls.custom_403'
handler400 = 'cbtis.urls.custom_400'