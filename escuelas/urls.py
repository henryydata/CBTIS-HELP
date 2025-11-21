from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='escuelas'),
    path('listar', views.listar, name='listar'),
    path('lista_escuelas', views.lista_escuelas, name='lista_escuelas'),
    path('agregar', views.agregar, name='agregar'),
    path('modificar/<id>/', views.modificar, name='modificar'),
    path('eliminar/<id>/', views.eliminar, name='eliminar'),
    path('<slug:slug>/', views.detalle, name='detalle')
]