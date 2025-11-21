from django.urls import path
from . import views

urlpatterns=[
    path('', views.categorias, name='categorias'),
    path('listar', views.listar, name='listar_categoria'),
    path('agregar', views.agregar, name='agregar_categoria'), 
    path('modificar/<id>/', views.modificar, name='modificar_categoria'),
    path('eliminar/<id>/', views.eliminar, name='eliminar_categoria')
]