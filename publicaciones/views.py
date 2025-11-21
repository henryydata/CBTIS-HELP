from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Publicacion
from comunidades.models import Comunidad
from .forms import PublicacionForm,PublicacionForm2
from django.contrib.auth.decorators import login_required

# listar publicaciones para vista general 
def listar_publicacion(request):
    publicaciones=Publicacion.objects.all()
    data={
        'publicaciones':publicaciones
    }
    return render(request, 'publicaciones/listar.html', data)

# listar publicaciones en una tabla con boton de eliminar y modificar  
def publicaciones(request):
    publicaciones=Publicacion.objects.all()
    data={
        'titulo': 'Publicaciones',
        'publicaciones': publicaciones
    }
    return render(request, 'publicaciones/publicaciones.html', data)

# agregar nuevas publicaciones para vista general 
def agregar(request):
    data={
        'form': PublicacionForm2()
    }
    if request.method=='POST':
        formulario=PublicacionForm2(request.POST, request.FILES)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user  
            publicacion.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_publicacion')
        else:
            data['form']=formulario
            messages.error(request, 'Error al guardar')
    return render(request, 'publicaciones/agregar.html', data)

# modificar publicaciones agregadas 
def modificar_publicacion(request, id):
    publicacion=get_object_or_404(Publicacion, id=id)
    data={
        'form':PublicacionForm2(instance=publicacion)
    }
    if request.method == 'POST':
        formulario=PublicacionForm2(request.POST, request.FILES, instance=publicacion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to='listar_publicacion')
        else:
            data['form']=formulario
            messages.error(request, 'Error al modificar')
    return render(request, 'publicaciones/modificar.html', data)

# eliminar publicaciones seleccionadas 
def eliminar(request, id):
    publicacion=get_object_or_404(Publicacion, id=id)
    publicacion.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect(to='listar_publicacion')