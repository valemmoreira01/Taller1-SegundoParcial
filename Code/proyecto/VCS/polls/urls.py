from django.http import HttpResponse
from django.urls import path
from .import views

app_name = 'polls'

urlpatterns = [
    #ex: /polls/
    path('', views.index, name='index'),
    #ex: /polls/1/
    path('<int:proyecto_id>/', views.detalle, name='detalle'),
    #ex: /polls/1/resultados/
    path('<int:proyecto_id>/resultados/', views.resultados, name='resultados'),
    #ex: /polls/1/calificacion/
    path('<int:proyecto_id>/calificacion/', views.calificacion, name='calificacion'),
]
