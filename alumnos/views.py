from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import AlumnoForm
from .models import Alumno
from django.contrib.auth.decorators import login_required

# lista los alumnos para una vista general para todos
def alumnos(request):
    data={
        'titulo': 'Alumnos'
    }
    return render(request, 'alumnos/alumnos.html', data)

# lista los alumnos en una tabla con los botones eliminar y modificar
def listar_alumno(request):
    alumnos=Alumno.objects.all()
    data={
        'title': 'Alumnos',
        'alumnos': alumnos
    }
    return render(request, 'alumnos/listar.html', data)

# Agrega un alumno 
def agregar_alumno(request):
    data={
        'form': AlumnoForm()
    }
    if request.method=='POST':
        formulario=AlumnoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_alumno')
        else:
            data['form']=formulario
            messages.error(request, 'Error al guardar')
    return render(request, 'alumnos/agregar.html', data)

# Modifica datos ya gregados a un alumno
def modificar_alumno(request, id):
    alumno=get_object_or_404(Alumno, id=id)
    data={
        'title': 'Modificar',
        'form': AlumnoForm(instance=alumno)
    }
    if request.method=='POST':
        formulario=AlumnoForm(data=request.POST,instance=alumno)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado exitosamente')
            return redirect(to='listar_alumno')
        else:
            data['form']=formulario
            messages.error(request, 'Error al modificar')
    return render(request, 'alumnos/modificar.html', data)

# Elimina el alumno seleccionado
def eliminar_alumno(request, id):
    alumno=get_object_or_404(Alumno, id=id)
    alumno.delete()
    messages.success(request, 'Eliminado exitosamente')
    return redirect(to='listar_alumno')