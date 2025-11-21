from django.shortcuts import render
from comunidades.models import Comunidad
from escuelas.models import Escuela

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