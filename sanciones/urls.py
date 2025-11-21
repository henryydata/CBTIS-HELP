from django.urls import path
from . import views

urlpatterns=[
    path('', views.sanciones, name='sanciones'),
    path('listar', views.listar, name='listar_sancion'),
    path('agregar', views.agregar, name='agregar_sancion'), 
    path('modificar/<id>/', views.modificar, name='modificar_sancion'),
    path('eliminar/<id>/', views.eliminar, name='eliminar_sancion')
]