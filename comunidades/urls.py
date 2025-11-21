from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='comunidades'),
    path('listar', views.listar_comunidad, name='listar_comunidad'),
    path('agregar', views.agregar_comunidad, name='agregar_comunidad'),
    path('modificar/<id>/', views.modificar_comunidad, name='modificar_comunidad'),
    path('eliminar/<id>/', views.eliminar_comunidad, name='eliminar_comunidad'),
    path('<slug:slug>/', views.ver_comunidad, name='ver_comunidad'),
    path('<slug:slug>/nuevo_post/', views.nuevo_post, name='nuevo_post_comunidad')
]