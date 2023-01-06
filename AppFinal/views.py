from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.core.files.storage import default_storage


#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth import login, authenticate

#from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS
#from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF 



# Create your views here.

def inicio (request):
    return render (request,"inicio.html")

def Profesores_index(request):
    return render (request, "Profesores_index.html")

def Materia_index(request):
    return render (request, "Materias_index.html")

def TrabajoPractico_index(request):
    return render (request, "TrabajoPractico_index.html")

def Materias_formulario(request):
    if request.method == "POST":
        form=MateriaForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            
            materia1=Materia(nombre=nombre)
            materia1.save()
            return render (request, "inicio.html")
        else:
            return render (request, "Materias_formulario.html",{"form":formulario})
    else:
        formulario=MateriaForm()
    
    
    return render (request, "Materias_formulario.html",{"form":formulario})


def TrabajoPractico_formulario(request):
    formulario = TrabajoForm()
    
    if request.method == "POST":
        form= TrabajoForm(request.POST, request.FILES)
        
        if form.is_valid():
            informacion=form.cleaned_data
            
            print(informacion)
            
            titulo1= informacion["titulo"]
            descripcion1= informacion["descripcion"]
            archivo1= informacion["archivo"]
            profesor1= informacion["profesor"]
            materia1= informacion["materia"]
        
            trabajo1= TrabajoPractico(titulo=titulo1, descripcion=descripcion1, archivo=archivo1, profesor=profesor1, materia=materia1)
            trabajo1.save()
            archivo = form.cleaned_data['archivo']
            ruta= f'archivos/ {titulo1}.pdf '
            
            default_storage.save(ruta, archivo)
            return render (request, "inicio.html")
        
        #else:
            #return render (request, "TrabajoPractico_formulario.html",{"form":formulario})
    else:
        formulario=TrabajoForm()

    return render (request, "TrabajoPractico_formulario.html", {"form":formulario})


def Profesores_formulario(request):
    
    
    if request.method == "POST":
        form=ProfesorForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            
            print(informacion)
            
            nombre1=informacion["nombre"]
            apellido1=informacion["apellido"]
            antiguedad1=informacion["antiguedad"]
            email1 = informacion["email"]
            materia1 =informacion["materia"]
            
            profesor1=Profesores(nombre=nombre1, apellido=apellido1, antiguedad=antiguedad1, email=email1, materia=materia1)
            profesor1.save()
            return render (request, "inicio.html")
        else:
            return render (request, "Profesores_formulario.html",{"form":formulario})
    else:
        formulario=ProfesorForm()
    
    
    return render (request, "Profesores_formulario.html",{"form":formulario})




#def TrabajoPractico_formulario(request):
#    if request.method == 'POST':
#        form = TrabajoForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
            #return render (request, "inicio.html")
            
#    else:
 #       form = TrabajoForm()
 #   return render(request, 'TrabajoPractico_formulario.html', {'form': form})


# Guardar el archivo en el directorio de archivos estáticos

def busquedaProfesor (request):
    return render (request, "busquedaProfesor.html")


def buscar(request):
    
    if "nombre" in request.GET:
        
        nombre= request.GET["nombre"]
        profesor=Profesores.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadosbusqueda.html", {"profesor":profesor})
    else:
        return render (request, "busquedaProfesor.html", {"mensaje":"Ingresa el nombre de un Profesor"})
     



def busquedaTrabajo (request):
    return render (request, "busquedaTrabajo.html")


def buscarTrabajo(request):
    
    if "titulo" in request.GET:
        
        titulo= request.GET["titulo"]
        trabajo=TrabajoPractico.objects.filter(titulo__icontains=titulo)
        return render(request, "resultadosbusquedaTrabajo.html", {"trabajo":trabajo})
    else:
        return render (request, "busquedaTrabajo.html", {"mensaje":"Ingresa una temática que coincida"})
     
#Vistas

def leerProfesores(request):
    profesores=Profesores.objects.all()
    return render (request, "leerProfesores.html", {"profesores":profesores})

def leerTrabajos(request):
    trabajos=TrabajoPractico.objects.all()
    return render (request, "leerTrabajos.html", {"trabajos":trabajos})


#Para ver si se puede descargar:


def descargar_archivo(request, nombre_archivo):
    # Abre el archivo en modo lectura binaria
    with open(f'archivos/{nombre_archivo}', 'rb') as archivo:
        # Crea una respuesta del servidor con el archivo
        response = HttpResponse(archivo.read(), content_type='application/pdf')
        # Agrega un encabezado 'Content-Disposition' para indicar que se está descargando un archivo
        response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
        return response

