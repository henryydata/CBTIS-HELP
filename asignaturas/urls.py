from django.urls import path
from . import views

urlpatterns=[
    path('', views.asignaturas, name='asignaturas'),
    path('listar', views.listar, name='listar_asignatura'),
    path('agregar', views.agregar, name='agregar_asignatura'), 
    path('modificar/<id>/', views.modificar, name='modificar_asignatura'),
    path('eliminar/<id>/', views.eliminar, name='eliminar_asignatura')
]