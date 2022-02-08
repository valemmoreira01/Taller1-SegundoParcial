from time import time, timezone
from django.db import models
from datetime import datetime

# Create your models here.
class Proyecto(models.Model):
    nombre_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Actividad(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre_actividad = models.CharField(max_length=200)
    calificacion = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_actividad