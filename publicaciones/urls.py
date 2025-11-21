from django.urls import path
from . import views

urlpatterns=[
    path('', views.publicaciones, name='publicaciones'),
    path('listar', views.listar_publicacion, name='listar_publicacion'),
    path('agregar', views.agregar, name='agregar_publicacion'),
    path('modificar/<id>/', views.modificar_publicacion, name='modificar_publicacion'),
    path('eliminar/<id>/', views.eliminar, name='eliminar_publicacion')
]