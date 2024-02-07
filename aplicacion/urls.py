from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cursos/', cursos, name="cursos"),
    path('entregables/', entregables, name="entregables"),
    #
    path('curso_form/', cursoForm, name="curso_form"),
    
    
    #________________________________________Profesores
    path('profesores/', profesores, name="profesores"),
    path('prof_form/', createProfesor, name="prof_form"),
    path('profesor_actualizar/<id_profesor>/', updateProfesor, name="profesorActualizar"),
    path('profesor_borrar/<id_profesor>', deleteProfesor, name="profesorBorrar"),
    
    path('buscar/', buscar, name = "buscar"),
    path('buscarCursos/', buscarCursos, name = "buscarCursos"),
    
    
    #___________________________________Estudiantes
    path('estudiantes/', EstudianteList.as_view(), name="estudiantes"),
    path('estudiante_create/', EstudianteCreate.as_view(), name="estudiante_create"),
    path('estudiante_update/<int:pk>/', EstudianteUpdate.as_view(), name="estudiante_update"),
    path('estudiante_delete/<int:pk>/', EstudianteDelete.as_view(), name="estudiante_delete"),

]
