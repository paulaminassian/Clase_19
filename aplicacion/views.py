from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html") #el render por default busca en templates, y ahi va a ir a la ruta aplicacion/html

def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto)

def profesores(request):
    return render(request, "aplicacion/profesores.html")

def estudiantes(request):
    return render(request, "aplicacion/estudiantes.html")

def entregables(request):
    return render(request, "aplicacion/entregables.html")