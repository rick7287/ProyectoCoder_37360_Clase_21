from django.urls import path
from .views import *


urlpatterns = [
    
    #path('curso/', curso, name='curso'),
    path('cursos/', curso_form, name='cursos'),
    path('profesores/', profesor_form, name='profesores'),
    path('estudiantes/', estudiante_form, name='estudiantes'),
    path('entregables/', entregable_form, name='entregables'),
    path('', inicio, name='inicio'),
    #path('curso_form/', curso_form, name='curso_form'),
    #path('profesor_form/', profesor_form, name='profesor_form'),
    #path('estudiante_form/', estudiante_form, name='estudiante_form'),
    #path('entregable_form/', entregable_form, name='entregable_form'),
    path('busqueda_comision/', busqueda_comision, name='busqueda_comision'),
    path('buscar/', buscar, name='buscar'),
    
]