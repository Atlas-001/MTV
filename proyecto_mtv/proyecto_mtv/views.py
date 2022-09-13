from django.http import HttpResponse
from django.template import loader
import datetime

def vista_familiar1 (request, nombre, edad, fecha):
    return HttpResponse("El primer familiar se llama "+nombre+", tiene "+edad+" años y nació el "+fecha+"")

def vista_familiar2 (request, nombre, edad, fecha):
    return HttpResponse("El segundo familiar se llama "+nombre+", tiene "+edad+" años y nació el "+fecha+"")

def vista_familiar3 (request, nombre, edad, fecha):
    return HttpResponse("El tercer familiar se llama "+nombre+", tiene "+edad+" años y nació el "+fecha+"")

def plantilla_familiar1(request):
    nom_ap="Juan Gómez"
    age=34
    fecha=datetime.date(1988,8,26)
    diccionario={'nombre_apellido1':nom_ap, 'edad1':age, 'fecha_nacimiento1': fecha}
    plantilla=loader.get_template('familiar.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def plantilla_familiar2(request):
    nom_ap="Pedro Ramírez"
    age=46
    fecha=datetime.date(1976,8,14)
    diccionario={'nombre_apellido2':nom_ap, 'edad2':age, 'fecha_nacimiento2': fecha}
    plantilla=loader.get_template('familiar.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def plantilla_familiar3(request):
    nom_ap="Julio López"
    age=62
    fecha=datetime.date(1960,4,12)
    diccionario={'nombre_apellido3':nom_ap, 'edad3':age, 'fecha_nacimiento3': fecha}
    plantilla=loader.get_template('familiar.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
