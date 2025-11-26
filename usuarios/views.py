from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

from alumnos.models import Alumno
from maestros.models import Maestro
from comunidades.models import Comunidad
from .forms import RegistroForm, CrearCuentaAlumnoForm, CrearCuentaMaestroForm

# registro de usuario 
def registro_usuario(request, perfil_id, tipo):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if tipo == 'alumno':
                perfil = Alumno.objects.get(id=perfil_id)
            else:
                perfil = Maestro.objects.get(id=perfil_id)
            perfil.user = user
            perfil.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form, "tipo": tipo})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            nombre = user.first_name or user.username
            request.session['bienvenido'] = nombre
            return redirect("index")
        else:
            return render(request, "login.html", {"error": "Usuario o contraseña incorrectos"})
    return render(request, "registration/login.html")

# regristrar cuentas alumnos  
def registro_alumno(request):
    if request.method == "POST":
        form = CrearCuentaAlumnoForm(request.POST)
        if form.is_valid():
            user=form.save()
            matricula=form.cleaned_data['matricula']
            try:
                alumno=Alumno.objects.get(matricula=matricula)
            except Alumno.DoesNotExist:
                messages.error(request, "⚠️ La matrícula no está registrada.")
                return render(request, "usuarios/registro_alumno.html", {"form": form})
            alumno.user=user
            alumno.save()
            messages.success(request, "Cuenta creada")
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, " Revisa los errores en el formulario.")
    else:
        form = CrearCuentaAlumnoForm()
    return render(request, "usuarios/registro_alumno.html", {"form": form})

# regristro de cuentas de maestros 
def registro_maestro(request):
    if request.method == "POST":
        form = CrearCuentaMaestroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.error(request, "⚠️ Revisa los errores en el formulario.")
    else:
        form = CrearCuentaMaestroForm()
    return render(request, "usuarios/registro_maestro.html", {"form": form})

def perfil_usuario(request,username):
    usuario=get_object_or_404(User, username=username)
    alumno=Alumno.objects.filter(user=usuario)
    data={
        'titulo':'Perfil',
        'usuario':usuario,
        'alumno':alumno
    }
    return render(request,'usuarios/usuario.html', data)