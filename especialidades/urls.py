from django.urls import path
from . import views

urlpatterns=[
    path('', views.especialidades, name='especialidades'),
    path('listar', views.listar, name='listar_especialidad'),
    path('agregar', views.agregar, name='agregar_especialidad'), 
    path('modificar/<id>/', views.modificar, name='modificar_especialidad'),
    path('eliminar/<id>/', views.eliminar, name='eliminar_especialidad')
]