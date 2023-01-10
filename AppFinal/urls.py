from django.contrib.auth.views import LogoutView
from django.urls import path
from AppFinal.views import *
from . import consumers

urlpatterns = [
    path('', inicio, name="inicio"),
    path('profesores/',Profesores_index, name="profesores"),
    path('materias/', Materia_index, name="materia"),
    path('trabajos/', TrabajoPractico_index, name="trabajos"),
    path('Materias_formulario/' , Materias_formulario, name="Materias_formulario"),
    path('TrabajoPractico_formulario/' , TrabajoPractico_formulario , name="TrabajoPractico_formulario"),
    path('Profesores_formulario/' , Profesores_formulario , name="Profesores_formulario"),
    path('busquedaProfesor/', busquedaProfesor, name="busquedaPorfesor"),
    path("buscar/", buscar, name="buscar"),
    path('busquedaTrabajo/', busquedaTrabajo, name="busquedaTrabajo"),
    path('buscarTrabajo/', buscarTrabajo, name="buscarTrabajo"),
    path("leerProfesores/", leerProfesores, name="leerProfesores"),
    path("leerTrabajos/", leerTrabajos, name="leerTrabajos"),
    path('descargar/<str:nombre_archivo>', descargar_archivo, name='descargar_archivo'),
    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor" ),
    path("eliminarTrabajo/<id>", eliminarTrabajo, name="eliminarTrabajo" ),
    path("editarProfesor/<id>", editarProfesor , name="editarProfesor"),
    path("editarTrabajo/<id>", editarTrabajo , name="editarTrabajo"),
    path("login/", login_request, name="login"),
    path("register/",register, name='register'),
    path("logout/",LogoutView.as_view(), name="logout"),
    path("editarUsuario/", editarUsuario, name="editarUsuario"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("sobrenosotros/", sobrenosotros , name="sobrenosotros"),
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
    path('chat/', chat, name='chat'),
    path('urlDisponibles/', urlDisponibles, name="urlDisponibles")


    

    
]
