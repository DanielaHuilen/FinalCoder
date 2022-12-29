from django.contrib.auth.views import LogoutView
from django.urls import path
from AppFinal.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('profesores/',Profesores_index, name="profesores"),
    path('materias', Materia_index, name="materia"),
    path('trabajos', TrabajoPractico_index, name="trabajos"),
    

    
]
