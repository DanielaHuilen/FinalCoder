from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.core.files.storage import default_storage


#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF 



# Create your views here.

def inicio (request):
    return render (request,"inicio.html")

def Profesores_index(request):
    return render (request, "Profesores_index.html")

def Materia_index(request):
    return render (request, "Materias_index.html")

def TrabajoPractico_index(request):
    return render (request, "TrabajoPractico_index.html")

@login_required
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

@login_required
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

@login_required
def Profesores_formulario(request, initial= None):
    
    
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
        formulario=ProfesorForm(initial=initial)
    
    
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
@login_required
def busquedaProfesor (request):
    return render (request, "busquedaProfesor.html")

@login_required
def buscar(request):
    
    if "nombre" in request.GET:
        
        nombre= request.GET["nombre"]
        profesor=Profesores.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadosbusqueda.html", {"profesor":profesor})
    else:
        return render (request, "busquedaProfesor.html", {"mensaje":"Ingresa el nombre de un Profesor"})
     


@login_required
def busquedaTrabajo (request):
    return render (request, "busquedaTrabajo.html")

@login_required
def buscarTrabajo(request):     
    
    if "titulo" in request.GET:
        
        titulo= request.GET["titulo"]
        trabajo=TrabajoPractico.objects.filter(titulo__icontains=titulo)
        return render(request, "resultadosbusquedaTrabajo.html", {"trabajo":trabajo})
    else:
        return render (request, "busquedaTrabajo.html", {"mensaje":"Ingresa una temática que coincida"})
     
#Vistas
@login_required
def leerProfesores(request):
    profesores=Profesores.objects.all()
    return render (request, "leerProfesores.html", {"profesores":profesores})

@login_required
def leerTrabajos(request):
    trabajos=TrabajoPractico.objects.all()
    return render (request, "leerTrabajos.html", {"trabajos":trabajos})


#Para ver si se puede descargar:


@login_required
def descargar_archivo(request, nombre_archivo):
    # Abre el archivo en modo lectura binaria
    with open(f'archivos/{nombre_archivo}', 'rb') as archivo:
        # Crea una respuesta del servidor con el archivo
        response = HttpResponse(archivo.read(), content_type='application/pdf')
        # Agrega un encabezado 'Content-Disposition' para indicar que se está descargando un archivo
        response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
        return response

#Eliminar

@login_required
def eliminarProfesor(request, id):
    profesor= Profesores.objects.get(id= id)
    profesor.delete()
    profesores= Profesores.objects.all()
    return render (request, "leerProfesores.html", {"mensaje":"Profesor eliminado correctamente", "profesores": profesores})


@login_required
def eliminarTrabajo(request, id):
    trabajo= TrabajoPractico.objects.get(id= id)
    trabajo.delete()
    trabajos= TrabajoPractico.objects.all()
    return render (request, "leerTrabajos.html", {"mensaje":"Trabajo Eliminado", "trabajos": trabajos})

#Editar

@login_required
def editarProfesor (request, id):
    profesor= Profesores.objects.get(id=id)
    if request.method=="POST":
        form= ProfesorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            
            profesor.nombre=informacion["nombre"]
            profesor.apellido=informacion["apellido"]
            profesor.antiguedad=informacion["antiguedad"]
            profesor.email=informacion["email"]
            profesor.materia=informacion["materia"]
            profesor.save()
            profesores=Profesores.objects.all()
            return render (request, "leerProfesores.html", {"mensaje":"Profesor editado correctamente", "profesores": profesores})
    else:
        formulario= ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "antiguedad":profesor.antiguedad,"email":profesor.email,"materia":profesor.materia})
    
   
    return render (request, "editarProfesor.html", {"form":formulario, "profesor":profesor})
    
    
@login_required
def editarTrabajo (request, id):    #revisar
    trabajo= TrabajoPractico.objects.get(id=id)
    
    if request.method=="POST":
        form= TrabajoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            
            trabajo.titulo=informacion["titulo"]
            trabajo.descripcion=informacion["descripcion"]
            trabajo.archivo=informacion["archivo"]
            trabajo.profesor=informacion["profesor"]
            trabajo.materia=informacion["materia"]
            trabajo.save()
            trabajos=TrabajoPractico.objects.all()
            return render (request, "leerTrabajos.html", {"mensaje":"Trabajo editado correctamente", "trabajos": trabajos})
    else:
        formulario= TrabajoForm(initial={"titulo":trabajo.titulo, "descripcion":trabajo.descripcion, "archivo":trabajo.archivo,"profesor":trabajo.profesor,"materia":trabajo.materia})
    return render (request, "editarTrabajo.html", {"form":formulario, "trabajo":trabajo})
    
    
#Login

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login (request, usuario)
                return render (request, "inicio.html", {"mensaje": f"Bienvenid@ Profe {usuario}" })
            else:
                return render (request, "login.html", {"mensaje":"usuario o contraseña incorrectos", 'form':form})
        
        else:
            return render (request, "login.html", {"mensaje":"usuario o contraseña incorrectos", 'form':form})
    
    else:
        form=AuthenticationForm
    return render (request, "login.html", {"form":form})



def register (request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password") #para que se logee directamente
            form.save()
            usuario=authenticate(username=username, password=clave) #para que se logee directamente
            login (request, usuario)#para que se logee directamente
            return render (request, "inicio.html",{'mensaje':f'Usuario {username} creado correctamente'})
        else:
            return render (request,"register.html",{"form":form, "mensaje":"Error al crear el usuario"})
  
    
    else:
        form= RegistroUsuarioForm()
    return render (request,"register.html",{"form":form})
