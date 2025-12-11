from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Asesoria, InscripcionAsesoria
from .forms import AsesoriaForm
from maestros.models import Maestro
from asignaturas.models import Asignatura
from categorias.models import Categoria
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import threading
from django.db.models import Q

def asesorias(request):
    hoy = timezone.localdate()
    maestro = request.GET.get("maestro")
    asignatura = request.GET.get("asignatura")
    categoria = request.GET.get("categoria")
    estado = request.GET.get("estado")
    asesorias = Asesoria.objects.filter(fecha__gte=hoy).order_by('fecha')
    if maestro:
        asesorias = asesorias.filter(maestro_id=maestro)

    if asignatura:
        asesorias = asesorias.filter(asignatura_id=asignatura)

    if categoria:
        asesorias = asesorias.filter(categoria_id=categoria)

    if estado == "1":
        asesorias = asesorias.filter(inscripcionasesoria__estado=True).distinct()

    elif estado == "0":
        asesorias = asesorias.exclude(inscripcionasesoria__estado=True).distinct()

    alumno = request.user.alumno

    inscripciones = {
        i.asesoria_id: i.estado
        for i in InscripcionAsesoria.objects.filter(alumno=alumno)
    }

    context = {
        "asesorias": asesorias,
        "inscripciones": inscripciones,
        "maestros": Maestro.objects.all(),
        "asignaturas": Asignatura.objects.all(),
        "categorias": Categoria.objects.filter(tipo='Asesoria'),
        "request": request, 
    }

    return render(request, "asesorias/asesorias.html", context)

# listar las asesorias en una tabla con los botones eliminar y modificar 
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

    data={
        "estado": "inscrito" if ins.estado else "cancelado",
        "cupos_restantes": asesoria.cupos_restantes,
        "mensaje": mensaje,
    }

    if ins.estado:
        hilo = threading.Thread(target=enviar_correo, args=(alumno, asesoria))
        hilo.start()

    return JsonResponse(data)

def enviar_correo(alumno, asesoria):
    try:
        html = render_to_string("emails/correo_inscripcion.html", {
            "alumno": alumno,
            "asesoria": asesoria
        })

        correo = EmailMessage(
            subject="Confirmación de inscripción",
            body=html,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[alumno.user.email],
        )

        correo.content_subtype = "html"
        correo.send(fail_silently=False)

    except Exception as e:
        print("ERROR AL ENVIAR CORREO:", e)
