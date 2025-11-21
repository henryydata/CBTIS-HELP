from django.urls import path
from . import views

urlpatterns=[
    path('', views.alumnos, name='alumnos'),
    path('listar', views.listar_alumno, name='listar_alumno'),
    path('agregar', views.agregar_alumno, name='agregar_alumno'),
    path('modificar/<id>/', views.modificar_alumno, name='modificar_alumno'),
    path('eliminar/<id>/', views.eliminar_alumno, name='eliminar_alumno')
]