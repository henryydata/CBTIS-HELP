from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import MaestroForm
from .models import Maestro
from asesorias.models import Asesoria, InscripcionAsesoria


def maestros(request):
    data={
        'titulo' : 'Maestros'
    }
    return render(request, 'maestros/index.html', data)

# listar maestros en una tabla con los botones de eliminar y modificar 
def listar_maestro(request):
    maestros=Maestro.objects.all()
    data={
        'titulo': 'Lista de Maestros',
        'maestros': maestros
    }
    return render(request, 'maestros/listar.html', data)

# agregar maestro nuevo 
def agregar_maestro(request):
    data={
        'form': MaestroForm()
    }
    if request.method=='POST':
        formulario=MaestroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_maestro')
        else:
            data['form']= formulario
            messages.error(request, 'Error al guardar')
    return render(request, 'maestros/agregar.html', data)

# modificar maestro agregado 
def modificar_maestro(request, id):
    maestro=get_object_or_404(Maestro,id=id)
    data={
        'title': 'Modificar',
        'form': MaestroForm(instance=maestro)
    }
    if request.method=='POST':
        formulario=MaestroForm(data=request.POST,instance=maestro)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado exitosamente')
            return redirect(to='listar_maestro')
        else:
            data['form']=formulario
            messages.error(request, 'Error al modificar')
    return render(request, 'maestros/modificar.html', data)

# eliminar maestro seleccionado
def eliminar_maestro(request,id):
    maestro=get_object_or_404(Maestro, id=id)
    maestro.delete()
    messages.success(request, 'Eliminado exitosamente')
    return redirect(to='listar_maestro')

def dashboard_maestro(request):
    maestro = Maestro.objects.get(user=request.user)

    asesorias = Asesoria.objects.filter(maestro=maestro)

    for a in asesorias:
        a.total_inscritos = InscripcionAsesoria.objects.filter(asesoria=a).count()
    data={
        'titulo':'Dashboard Maestro',
        'maestro': maestro,
        'asesorias': asesorias
    }
    return render(request, "maestros/dashboard.html", data)

def inscritos_asesoria(request, id):
    asesoria = Asesoria.objects.get(id=id)
    maestro = Maestro.objects.get(user=request.user)

    if asesoria.maestro != maestro:
        return HttpResponseForbidden("No puedes ver esta asesoría.")

    inscritos = InscripcionAsesoria.objects.filter(asesoria=asesoria).select_related("alumno")

    paginator = Paginator(inscritos, 10)  # 10 por página
    page = request.GET.get('page')
    inscritos_pagina = paginator.get_page(page)
    data={
        'titulo': f'Inscritos en {asesoria.nombre}',
        "asesoria": asesoria,
        "inscritos": inscritos_pagina,
    }
    return render(request, "maestros/inscritos.html", data)
