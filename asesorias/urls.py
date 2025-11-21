from django.urls import path
from . import views

urlpatterns=[
    path('', views.asesorias, name='asesorias'),
    path('listar', views.listar, name='listar_asesoria'),
    path('agregar', views.agregar, name='agregar_asesoria'), 
    path('modificar/<id>/', views.modificar, name='modificar_asesoria'),
    path('eliminar/<id>/', views.eliminar, name='eliminar_asesoria'),
    path('<int:id>/toggle/', views.toggle_inscripcion, name='toggle_inscripcion'),
]