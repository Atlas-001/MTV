from pipes import Template
from unittest import loader
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Template, Context, loader
def saludo (request):
    return HttpResponse("<h3>Hola Django - Coder</h3>")

def sumar (request):
    return HttpResponse ("En esta pagina voy a sumar numeros.")

def miNombre(self, nombre):
    texto = f"mi nombre es: {nombre}"
    return HttpResponse(texto)

def probandoTemplate(self):
    """miHtml = open("D:/CoderPy/proyecto_mtv/proyecto_mtv/plantillas/template.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)"""
    plantilla = loader.get_template("template.html")
    documento = plantilla.render()
    return HttpResponse(documento)
