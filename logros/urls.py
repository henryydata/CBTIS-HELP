from django.urls import path
from . import views

urlpatterns=[
    path('', views.logros, name='logros'),
    path('listar', views.listar, name='listar_logro'),
    path('agregar', views.agregar, name='agregar_logro'), 
    path('modificar/<id>/', views.modificar, name='modificar_logro'),
    path('eliminar/<id>/', views.eliminar, name='eliminar_logro')
]