from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiares
import datetime

def familiar_1(request):
    familiar_1=Familiares(nombre_apellido="Juan Gómez", edad=34)
    texto=f"El primer familiar se llama {familiar_1.nombre_apellido} y tiene {familiar_1.edad} años"
    return HttpResponse(texto)

def familiar_2(request):
    familiar_2=Familiares(nombre_apellido="Pedro Ramírez", edad=46)
    texto=f"El segundo familiar se llama {familiar_2.nombre_apellido} y tiene {familiar_2.edad} años"
    return HttpResponse(texto)

def familiar_3(request):
    familiar_3=Familiares(nombre_apellido="Julio López", edad=62)
    texto=f"El tercer familiar se llama {familiar_3.nombre_apellido} y tiene {familiar_3.edad} años"
    return HttpResponse(texto)