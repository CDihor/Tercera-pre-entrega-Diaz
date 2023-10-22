#Views
from django.shortcuts import render
from django.http import HttpResponse

def lista_objetos(request):
    # Código para listar objetos
    return HttpResponse("Listando objetos")

def agregar_objeto(request):
    # Código para agregar objetos
    return HttpResponse("Agregando objeto")

def buscar_objeto(request):
    # Código para buscar objetos
    return HttpResponse("Buscando objeto")


