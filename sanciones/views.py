from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Sancion
from .forms import SancionForm

# listar sanciones para vista general 
def sanciones(request):
    sancion=Sancion.objects.all()
    data={
        'titulo':'Sancion',
        'sanciones':sancion
    }
    return render(request, 'sanciones/listar.html', data)

# listar sanciones en una tabla con boton de eliminar y modificar 
def listar(request):
    sancion=Sancion.objects.all()
    data={
        'titulo':'sancion',
        'sanciones':sancion
    }
    return render(request, 'sanciones/listar.html', data)

# agregar nuevas sanciones 
def agregar(request):
    data={
        'titulo':'Agregar',
        'formulario':SancionForm()
    }
    if request.method == 'POST':
        formulario=SancionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_sancion')
        else:
            data['formulario']=SancionForm()
            messages.error(request, 'Error al guardar')
    return render(request, 'sanciones/agregar.html', data)

# modificar las sanciones agregadas 
def modificar(request, id):
    sancion=get_object_or_404(Sancion, id=id)
    data={
        'titulo':'Modificar',
        'formulario':SancionForm(instance=sancion)
    }
    if request.method=='POST':
        formulario=SancionForm(instance=sancion, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado exitosamente')
            return redirect(to='listar_sancion')
        else:
            data['formulario']=SancionForm()
            messages.error(request, 'Error al modificar')
    return render(request, 'sanciones/modificar.html', data)

# eliminar sanciones seleccionadas 
def eliminar(request, id):
    sancion=get_object_or_404(Sancion, id=id)
    sancion.delete()
    messages.success(request, 'Eliminado exitosamente')
    return redirect(to='listar_sancion')
