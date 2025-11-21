from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Asesoria, InscripcionAsesoria
from .forms import AsesoriaForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from alumnos.models import Alumno

# listar las asesorias 
def asesorias(request):
    asesorias = Asesoria.objects.all()
    alumno = request.user.alumno

    inscripciones = {
        i.asesoria.id: i.estado
        for i in InscripcionAsesoria.objects.filter(alumno=alumno)
    }

    return render(request, "asesorias/asesorias.html", {
        "asesorias": asesorias,
        "inscripciones": inscripciones,
    })

# lisatar las asesorias en una tabla con los botones eliminar y modificar 
def listar(request):
    asesorias=Asesoria.objects.all()
    data={
        'titulo':'Asesorias',
        'asesorias': asesorias
    }
    return render(request, 'asesorias/listar.html', data)

# Agregar asesoria 
def agregar(request):
    data={
        'titulo':'Agregar',
        'formulario':AsesoriaForm()
    }
    if request.method == 'POST':
        formulario=AsesoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_asesoria')
        else:
            data['formulario']=AsesoriaForm()
            messages.error(request, 'Error al guardar')
            return redirect(to='listar_asesoria')
    return render(request, 'asesorias/agregar.html', data)

# Modifica datos agregados a la asesoria 
def modificar(request, id):
    asesoria=get_object_or_404(Asesoria, id=id)
    data={
        'titulo':'Modificar',
        'formulario':AsesoriaForm(instance=asesoria)
    }
    if request.method=='POST':
        formulario=AsesoriaForm(instance=asesoria, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Guardado exitosamente')
            return redirect(to='listar_asesoria')
        else:
            data['formulario']=AsesoriaForm()
            messages.error(request, 'Error al modificar')
    return render(request, 'asesorias/modificar.html', data)

# Elimina asesoria seleccionada 
def eliminar(request, id):
    asesoria=get_object_or_404(Asesoria, id=id)
    asesoria.delete()
    messages.success(request,'Eliminado exitosamente')
    return redirect(to='listar_asesoria')

@require_POST
def toggle_inscripcion(request, id):
    asesoria = get_object_or_404(Asesoria, id=id)
    alumno = request.user.alumno

    ins, created = InscripcionAsesoria.objects.get_or_create(
        alumno=alumno,
        asesoria=asesoria,
        defaults={"estado": True}
    )

    if not created:
        ins.estado = not ins.estado
        ins.save()

    mensaje = "Inscripción realizada exitosamente" if ins.estado else "Inscripción cancelada"

    return JsonResponse({
        "estado": "inscrito" if ins.estado else "cancelado",
        "cupos_restantes": asesoria.cupos_restantes,
        "mensaje": mensaje,
    })

