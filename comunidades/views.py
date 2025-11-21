from django.shortcuts import render, redirect, get_object_or_404
from .models import Comunidad
from .forms  import ComunidadForm
from publicaciones.models import Publicacion
from publicaciones.forms import PublicacionForm
from  django.contrib import messages

def index(request):
    comunidades=Comunidad.objects.all()
    data={
        'titulo': 'Comunidades',
        'comunidades': comunidades
    }
    return render(request, 'comunidades/index.html', data)

# listar comunidades en una tabla 
def listar_comunidad(request):
    comunidades=Comunidad.objects.all()
    data={
        'titulo': 'Lista de comunidades',
        'comunidades' : comunidades
    }
    return render(request, 'comunidades/listar.html', data)

# agregar conmunidades 
def agregar_comunidad(request):
    data = {
        'titulo': 'Agregar comunidad',
        'form': ComunidadForm()
    }
    if request.method == 'POST':
        formulario = ComunidadForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect('listar_comunidad')
        else:
            messages.error(request, 'Error al guardar')
            data['form'] = formulario
    return render(request, 'comunidades/agregar.html', data)

# modificar las comunidades agregadas 
def modificar_comunidad(request, id):
    comunidad = get_object_or_404(Comunidad, id=id)
    data = {
        'titulo': 'Modificar comunidad',
        'form': ComunidadForm(instance=comunidad)
    }
    if request.method == 'POST':
        formulario = ComunidadForm(request.POST, request.FILES, instance=comunidad)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificada exitosamente')
            return redirect('listar_comunidad')
        else:
            messages.error(request, 'Error al modificar')
            data['form'] = formulario
    return render(request, 'comunidades/modificar.html', data)

# eliminar comunidad se leccionada 
def eliminar_comunidad(request,id):
    comunidad=get_object_or_404(Comunidad, id=id)
    comunidad.delete()
    messages.success(request, 'Eliminada correctamente')
    return redirect(to='listar_comunidad')


def ver_comunidad(request, slug):
    comunidad = get_object_or_404(Comunidad, slug=slug)
    publicaciones = Publicacion.objects.filter(comunidad=comunidad).order_by('-fecha_hora')

    context = {
        'comunidad': comunidad,
        'publicaciones': publicaciones
    }
    return render(request, 'comunidades/comunidad.html', context)

# agregar un nuevo post 
def nuevo_post(request, slug):
    comunidad = get_object_or_404(Comunidad, slug=slug)
    form = PublicacionForm()
    
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.comunidad = comunidad
            publicacion.save()
            messages.success(request, 'Publicación creada correctamente')
            return redirect('ver_comunidad', slug=comunidad.slug)
        else:
            messages.error(request, 'Error al crear la publicación')
    
    return render(request, 'publicaciones/agregar.html', {'form': form, 'comunidad': comunidad})
