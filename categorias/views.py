from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria
from .forms import CategoriaForm

# listar categorias en una tabla con boton de eliminar y modificar 
def categorias(request):
    categoria=Categoria.objects.all()
    data={
        'titulo':'Categoria',
        'categorias':categoria
    }
    return render(request, 'categorias/listar.html', data)

# listar las categorias en una tabla con los botones eliminar y modificar 
def listar(request):
    categoria=Categoria.objects.all()
    data={
        'titulo':'Categoria',
        'categorias':categoria
    }
    return render(request, 'categorias/listar.html', data)

# Agregar categorias 
def agregar(request):
    data={
        'titulo':'Agregar',
        'formulario':CategoriaForm()
    }
    if request.method == 'POST':
        formulario=CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_categoria')
        else:
            data['formulario']=CategoriaForm()
            messages.error(request, 'Error al guardar')
    return render(request, 'categorias/agregar.html', data)

# Modificar categorias 
def modificar(request, id):
    categoria=get_object_or_404(Categoria, id=id)
    data={
        'titulo':'Modificar',
        'formulario':CategoriaForm(instance=categoria)
    }
    if request.method=='POST':
        formulario=CategoriaForm(instance=categoria, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado exitosamente')
            return redirect(to='listar_categoria')
        else:
            data['formulario']=CategoriaForm()
            messages.error(request, 'Error al modificar')
    return render(request, 'categorias/modificar.html', data)

# Eliminar categoria seleccionada 
def eliminar(request, id):
    categoria=get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, 'Eliminado exitosamente')
    return redirect(to='listar_categoria')