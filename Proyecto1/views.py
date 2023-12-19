from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime as dt
import random

def bienvenida(request):
    return HttpResponse("Bienvenido")


def hora_actual(request):

    ahora = dt.datetime.now()
    
    mensaje = f"{ahora.hour}:{ahora.minute}:{ahora.second}"
    
    return HttpResponse(mensaje)


def saludar(request, name):
    mensaje = f"Hola {name}. Mucho gusto!"

    return HttpResponse(mensaje)


def inicio(request):

    #f = open(r"C:\Users\dalev\Desktop\CH - 50195\PythonProyecto1\Proyecto1\Proyecto1\Templates\inicio.html")
    #f = open("C:/Users/dalev/Desktop/CH - 50195/PythonProyecto1/Proyecto1/Proyecto1/Templates/inicio.html")
    #plantilla = Template(f.read())
    #f.close()
    #aleatorio = random.randint(1,100)
    #info = {"numero":aleatorio}
    #contexto = Context(info)
    #plantilla = plantilla.render(contexto) #pasando la info del diccionario al html 

    plantilla = loader.get_template("inicio.html")
    aleatorio = random.randint(1,10)
    info = {"numero":aleatorio}
    plantilla = plantilla.render(info)
    
    return HttpResponse(plantilla)


