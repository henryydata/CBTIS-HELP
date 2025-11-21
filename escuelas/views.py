from django.shortcuts import render, redirect, get_object_or_404
from .forms import EscuelaForm
from .models import Escuela
from especialidades.models import Especialidad
from maestros.models import Maestro
from django.contrib import messages
from django.db.models import Q

def index(request):
    escuelas=Escuela.objects.all()
    data={
        'titulo' : 'Escuelas',
        'escuelas': escuelas
    }
    return render(request, 'escuelas/escuelas.html', data)

def lista_escuelas(request):
    query = request.GET.get("q")  # toma lo que el usuario escribe en el buscador
    if query:
        escuelas = Escuela.objects.filter(
            Q(nombre__icontains=query) |
            Q(plantel__icontains=query) |
            Q(direccion__icontains=query)
        ).distinct()
    else:
        escuelas = Escuela.objects.all()

    return render(request, "escuelas/escuelas.html", {
        "escuelas": escuelas,
        "query": query
    })


# listar escuelas en una tabla con boton de eliminar y modificar 
def listar(request):
    escuelas=Escuela.objects.all()
    data={
        'titulo' : 'Escuelas',
        'escuelas': escuelas
    }
    return render(request, 'escuelas/listar.html', data)

# agregar escuelas nuevas 
def agregar(request):
    data={
        'titulo': 'Agregar',
        'form': EscuelaForm()
    }
    if request.method=='POST':
        formulario=EscuelaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar')
        else:
            data['form']=formulario
            messages.error(request, 'Error al guardar')
    return render(request, 'escuelas/agregar.html', data)

# modificar las escuelas agregadas 
def modificar(request, id):
    escuela=get_object_or_404(Escuela, id=id)
    data={
        'titulo' : 'Modificar',
        'form' : EscuelaForm(instance=escuela)
    }
    if request.method=='POST':
        formulario=EscuelaForm(data=request.POST, instance=escuela)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado exitosamente")
            return redirect(to='listar')
        else:
            data['form']=formulario
            messages.error(request, "Error al modificar")
    return render(request, 'escuelas/modificar.html', data)

# eliminar escuelas seleccionadas 
def eliminar(request, id):
    escuela=get_object_or_404(Escuela, id=id)
    escuela.delete()
    messages.success(request, "Eliminado exitosamente")
    return redirect(to='listar')

def detalle(request, slug):
    escuela=get_object_or_404(Escuela, slug=slug)
    especialidad=Especialidad.objects.filter(escuela=escuela)
    maestro=Maestro.objects.filter(escuela=escuela)
    data={
        'titulo' : 'Detalle',
        'escuela' : escuela,
        'especialidades' : especialidad,
        'maestros' : maestro
    }
    return render(request, 'escuelas\escuela.html', data)