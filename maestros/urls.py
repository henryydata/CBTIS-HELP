from django.urls import path
from . import views

urlpatterns=[
    path('', views.maestros, name='maestros'),
    path('listar', views.listar_maestro, name='listar_maestro'),
    path('agregar', views.agregar_maestro, name='agregar_maestro'),
    path('modificar/<id>/', views.modificar_maestro, name='modificar_maestro'),
    path('eliminar/<id>/', views.eliminar_maestro, name='eliminar_maestro'),
    path('asesoria/<id>/inscritos/', views.inscritos_asesoria, name='inscritos_asesoria'),
    path('dashboard/', views.dashboard_maestro, name='dashboard_maestro')
]