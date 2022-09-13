from datetime import date
from django.db import models
import datetime

class Familiares(models.Model):
    nombre_apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField(null=True, blank=True)
