from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Logro
from .forms import LogroForm

def logros(request):
    logro=Logro.objects.all()
    data={
        'titulo':'Logro',
        'logros':logro
    }
    return render(request, 'logros/listar.html', data)

# listar logros en una tabla 
def listar(request):
    logro=Logro.objects.all()
    data={
        'titulo':'logro',
        'logros':logro
    }
    return render(request, 'logros/listar.html', data)

# agregar logros  
def agregar(request):
    data={
        'titulo':'Agregar',
        'formulario':LogroForm()
    }
    if request.method == 'POST':
        formulario=LogroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_logro')
        else:
            data['formulario']=LogroForm()
            messages.error(request, 'Error al guardar')
    return render(request, 'logros/agregar.html', data)

# modificar logros agregados 
def modificar(request, id):
    logro=get_object_or_404(Logro, id=id)
    data={
        'titulo':'Modificar',
        'formulario':LogroForm(instance=logro)
    }
    if request.method=='POST':
        formulario=LogroForm(instance=logro, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado exitosamente')
            return redirect(to='listar_logro')
        else:
            data['formulario']=LogroForm()
            messages.error(request, 'Error al modificar')
    return render(request, 'logros/modificar.html', data)

# eliminar logros selecionados 
def eliminar(request, id):
    logro=get_object_or_404(Logro, id=id)
    logro.delete()
    messages.success(request, 'Eliminado exitosamente')
    return redirect(to='listar_logro')
