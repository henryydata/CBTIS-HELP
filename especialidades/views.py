from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Especialidad
from .forms import EspecialidadForm

# listar especialidades para vista general 
def especialidades(request):
    especialidad=Especialidad.objects.all()
    data={
        'titulo':'Especialidad',
        'especialidades':especialidad
    }
    return render(request, 'especialidades/listar.html', data)

# listar specialidades en una tabla con boton de eliminar y modificar  
def listar(request):
    especialidad=Especialidad.objects.all()
    data={
        'titulo':'especialidad',
        'especialidades':especialidad
    }
    return render(request, 'especialidades/listar.html', data)

# agregar nuevas especialiidades 
def agregar(request):
    data={
        'titulo':'Agregar',
        'formulario':EspecialidadForm()
    }
    if request.method == 'POST':
        formulario=EspecialidadForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_especialidad')
        else:
            data['formulario']=EspecialidadForm()
            messages.error(request, 'Error al guardar')
    return render(request, 'especialidades/agregar.html', data)

# modificar especialidades agregadas 
def modificar(request, id):
    especialidad=get_object_or_404(Especialidad, id=id)
    data={
        'titulo':'Modificar',
        'formulario':EspecialidadForm(instance=especialidad)
    }
    if request.method=='POST':
        formulario=EspecialidadForm(instance=especialidad, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado exitosamente')
            return redirect(to='listar_especialidad')
        else:
            data['formulario']=EspecialidadForm()
            messages.error(request, 'Error al modificar')
    return render(request, 'especialidades/modificar.html', data)

# eliminar especialidad seleccionada 
def eliminar(request, id):
    especialidad=get_object_or_404(Especialidad, id=id)
    especialidad.delete()
    messages.success(request, 'Eliminado exitosamente')
    return redirect(to='listar_especialidad')