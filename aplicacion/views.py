from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView



# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html") #el render por default busca en templates, y ahi va a ir a la ruta aplicacion/html


#________________________________________Cursos

def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto)

def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos}
        return render(request, "aplicacion/cursos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

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

#_____________________________________________________________Profesores 

def profesores(request):
    contexto = {'profesores': Profesor.objects.all()}
    return render(request, "aplicacion/profesores.html", contexto)

def createProfesor(request):
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            prof_nombre = miForm.cleaned_data.get("nombre")
            prof_apellido = miForm.cleaned_data.get("apellido")
            prof_email = miForm.cleaned_data.get("email")
            prof_profesion = miForm.cleaned_data.get("profesion")
            profe = Profesor(nombre=prof_nombre, apellido=prof_apellido, email = prof_email, profesion = prof_profesion)
            profe.save()
            return redirect(reverse_lazy('profesores'))
    else:  
        miForm = ProfesorForm()
    
    return render(request, "aplicacion/profesorForm.html", {"form": miForm})

def updateProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data.get('nombre')
            profesor.apellido = miForm.cleaned_data.get('apellido')
            profesor.email = miForm.cleaned_data.get('email')
            profesor.profesion = miForm.cleaned_data.get('profesion') 
            profesor.save()
            return redirect(reverse_lazy('profesores'))   
    else:
        miForm = ProfesorForm(initial={
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'email': profesor.email,
            'profesion': profesor.profesion,
        })
    return render(request, "aplicacion/profesorForm.html", {'form': miForm})

def deleteProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    return redirect(reverse_lazy('profesores'))

#___________________Entregables

def entregables(request):
    return render(request, "aplicacion/entregables.html")



#___________________Estudiantes

def estudiantes(request):
    return render(request, "aplicacion/estudiantes.html")

class EstudianteList(ListView):
    model = Estudiante 

class EstudianteCreate(CreateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes')
    
    
class EstudianteUpdate(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes')
    
    
class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')

    
