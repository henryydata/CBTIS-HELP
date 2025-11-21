from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('create_account/', auth_views.LoginView.as_view(template_name='usuarios/create_account.html'), name='create_account'),
    path("registro_alumno/", views.registro_alumno, name="registro_alumno"),
    path('registro_maestro/', views.registro_maestro, name='registro_maestro'),
    path('<str:username>/', views.perfil_usuario, name='perfil_usuario')
]
