from django.urls import path
from .views import *


urlpatterns = [
    
    path('curso/', curso, name='curso'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
    path('', inicio, name='inicio'),
    
]