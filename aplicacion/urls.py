from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    #
    path('curso_form/', cursoForm, name="curso_form"),
    path('prof_form/', profesorForm, name="prof_form"),
    
    path('buscar/', buscar, name = "buscar"),
    path('buscarCursos/', buscarCursos, name = "buscarCursos"),
]
