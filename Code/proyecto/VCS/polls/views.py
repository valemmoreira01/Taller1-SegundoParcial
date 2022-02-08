from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto

# Create your views here.
def index(request):
    proyectos=Proyecto.objects.all()
    return render(request, 'polls/index.html', {'latest_proyecto_list': proyectos})

def detalle(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    return render(request, 'polls/detalle.html', {'proyecto': proyecto})

def resultados(request, proyecto_id):
    return HttpResponse(f'Estas viendo la calificacion del proyecto numero: {proyecto_id}')

def calificacion (request, proyecto_id):
    return HttpResponse(f'Estas calificando el proyecto numero: {proyecto_id}')