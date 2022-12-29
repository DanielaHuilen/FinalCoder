from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import *

#from django.urls import reverse_lazy

#from AppCoder.forms import CursoForm, ProfeForm, RegistroUsuarioForm, UserEditForm, AvatarForm

#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth import login, authenticate

#from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS
#from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF 

#from django.shortcuts import render


# Create your views here.

def inicio (request):
    return render (request,"inicio.html")

def Profesores_index(request):
    return render (request, "Profesores_index.html")

def Materia_index(request):
    return render (request, "Materias_index.html")

def TrabajoPractico_index(request):
    return render (request, "TrabajoPractico_index.html")
