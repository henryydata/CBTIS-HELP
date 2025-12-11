from django.shortcuts import render
from comunidades.models import Comunidad
from escuelas.models import Escuela
from alumnos.models import Alumno
from maestros.models import Maestro
from asesorias.models import Asesoria, InscripcionAsesoria


def index(request):
    bienvenido = request.session.pop('bienvenido', None)
    escuelas=Escuela.objects.all()
    comunidades=Comunidad.objects.all()
    data={ 
        'comunidades':comunidades,
        'escuelas':escuelas,
        'bienvenido':bienvenido
    }
    return render(request, 'index.html', data)

def dashboard(request):
    alumnos=Alumno.objects.count()
    maestros=Maestro.objects.count()
    asesorias_activas=InscripcionAsesoria.objects.filter(estado=True).count
    inscripciones=InscripcionAsesoria.objects.count()
    ultimas_inscripciones=Asesoria.objects.order_by('-fecha')[:10]

    data = {
    "total_alumnos": alumnos,
    "total_maestros": maestros,
    "total_asesorias_activas": asesorias_activas,
    "total_inscripciones": inscripciones,
    "ultimas_inscripciones": ultimas_inscripciones,
}

    return render(request, 'admin/dashboard.html', data)

def buscar(request):
    query=request.GET.get('q','')
    alumnos=Alumno.objects.filter(nombre__icontains=query)
    maestros=Maestro.objects.filter(nombre__icontains=query)
    asesorias=Asesoria.objects.filter(nombre__icontains=query)
    data={
        'alumnos':alumnos,
        'maestros':maestros,
        'asesorias':asesorias,
        'query':query
    }
    return render(request, 'buscar.html', data)