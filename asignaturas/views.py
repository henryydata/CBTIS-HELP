from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Asignatura
from .forms import AsignaturaForm

# listar las asignaturas para una vista gerneral para todos 
def asignaturas(request):
    asignatura=Asignatura.objects.all()
    data={
        'titulo':'Asignatura',
        'asignaturas':asignatura
    }
    return render(request, 'asignaturas/listar.html', data)

# listar las asignaturas en una tabla con los botones eliminar y modificar 
def listar(request):
    asignatura=Asignatura.objects.all()
    data={
        'titulo':'Asignatura',
        'asignaturas':asignatura
    }
    return render(request, 'asignaturas/listar.html', data)

# Agregar asignatura 
def agregar(request):
    data={
        'titulo':'Agregar',
        'formulario':AsignaturaForm()
    }
    if request.method == 'POST':
        formulario=AsignaturaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_asignatura')
        else:
            data['formulario']=AsignaturaForm()
            messages.error(request, 'Error al guardar')
    return render(request, 'asignaturas/agregar.html', data)

# Modificar la asignatura agregada 
def modificar(request, id):
    asignatura=get_object_or_404(Asignatura, id=id)
    data={
        'titulo':'Modificar',
        'formulario':AsignaturaForm(instance=asignatura)
    }
    if request.method=='POST':
        formulario=AsignaturaForm(instance=asignatura, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_asignatura')
        else:
            data['formulario']=AsignaturaForm()
            messages.error(request, 'Error al modificar')
    return render(request, 'asignaturas/modificar.html', data)

# Elimina las asignaturas seleccionadas 
def eliminar(request, id):
    asignatura=get_object_or_404(Asignatura, id=id)
    asignatura.delete()
    messages.success(request, 'Eliminado exitosamente')
    return redirect(to='listar_asignatura')


