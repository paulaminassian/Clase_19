from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html") #el render por default busca en templates, y ahi va a ir a la ruta aplicacion/html

def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto)

def profesores(request):
    contexto = {'profesores': Profesor.objects.all()}
    return render(request, "aplicacion/profesores.html", contexto)

def estudiantes(request):
    return render(request, "aplicacion/estudiantes.html")

def entregables(request):
    return render(request, "aplicacion/entregables.html")

def cursoForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get("nombre")
            curso_comision = miForm.cleaned_data.get("comision")
            curso = Curso(nombre=curso_nombre, comision=curso_comision)
            curso.save()
            return render(request, "aplicacion/home.html")
    else:  
        miForm = CursoForm()
    
    return render(request, "aplicacion/cursoForm.html", {"form": miForm})


def profesorForm(request):
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            prof_nombre = miForm.cleaned_data.get("nombre")
            prof_apellido = miForm.cleaned_data.get("apellido")
            prof_email = miForm.cleaned_data.get("email")
            prof_profesion = miForm.cleaned_data.get("profesion")
            profesor = Profesor(nombre=prof_nombre, apellido=prof_apellido, email = prof_email, profesion = prof_profesion)
            profesor.save()
            return render(request, "aplicacion/home.html") # a que pagina me devuelve
    else:  
        miForm = ProfesorForm()
    
    return render(request, "aplicacion/profesorForm.html", {"form": miForm})

def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos}
        return render(request, "aplicacion/cursos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")
        