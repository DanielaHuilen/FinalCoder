from django.shortcuts import render, redirect
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
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/Avatarpordefecto.png"
    return imagen



def inicio (request):
    lista=Avatar.objects.filter(user=request.user)
    
    return render (request, "inicio.html", {"imagen":obtenerAvatar(request)})
    

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
            return render (request, "inicio.html", {"mensaje":"Materia seleccionada correctamente"})
        else:
            return render (request, "Materias_formulario.html",{"form":formulario,"imagen":obtenerAvatar(request),})
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
            return render (request, "inicio.html",{"mensaje":"Trabajo Práctico guardado correctamente"})
        
        #else: 
            #return render (request, "TrabajoPractico_formulario.html",{"form":formulario})
    else:
        formulario=TrabajoForm()

    return render (request, "TrabajoPractico_formulario.html", {"form":formulario, "imagen":obtenerAvatar(request)} )

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
            return render (request, "inicio.html", {"mensaje":"Profesor creado correctamente"})
        else:
            return render (request, "Profesores_formulario.html",{"form":formulario})
    else:
        formulario=ProfesorForm(initial=initial)
    
    
    return render (request, "Profesores_formulario.html",{"form":formulario,"imagen":obtenerAvatar(request) })




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
        return render (request, "busquedaProfesor.html", {"mensaje":"Ingresa el nombre de un Profesor", "imagen":obtenerAvatar(request)})
     


@login_required
def busquedaTrabajo (request):
    return render (request, "busquedaTrabajo.html")

@login_required
def buscarTrabajo(request):     
    
    if "titulo" in request.GET:
        
        titulo= request.GET["titulo"]
        trabajo=TrabajoPractico.objects.filter(titulo__icontains=titulo)
        return render(request, "resultadosbusquedaTrabajo.html", {"trabajo":trabajo, "imagen":obtenerAvatar(request)})
    else:
        return render (request, "busquedaTrabajo.html", {"mensaje":"Ingresa una temática que coincida", "imagen":obtenerAvatar(request)})
     
#Vistas
@login_required
def leerProfesores(request):
    profesores=Profesores.objects.all()
    return render (request, "leerProfesores.html", {"profesores":profesores , "imagen":obtenerAvatar(request)})

@login_required
def leerTrabajos(request):
    trabajos=TrabajoPractico.objects.all()
    return render (request, "leerTrabajos.html", {"trabajos":trabajos, "imagen":obtenerAvatar(request)})


#Para ver si se puede descargar:


@login_required
def descargar_archivo(request, nombre_archivo):
    
    with open(f'media/{nombre_archivo}', 'rb') as archivo:
        
        response = HttpResponse(archivo.read(), content_type='application/pdf')
      
        response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
        return response

#Eliminar

@login_required
def eliminarProfesor(request, id):
    profesor= Profesores.objects.get(id= id)
    profesor.delete()
    profesores= Profesores.objects.all()
    return render (request, "leerProfesores.html", {"mensaje":"Profesor eliminado correctamente", "profesores": profesores, "imagen":obtenerAvatar(request)})


@login_required
def eliminarTrabajo(request, id):
    trabajo= TrabajoPractico.objects.get(id= id)
    trabajo.delete()
    trabajos= TrabajoPractico.objects.all()
    return render (request, "leerTrabajos.html", {"mensaje":"Trabajo Eliminado", "trabajos": trabajos, "imagen":obtenerAvatar(request)})

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
            return render (request, "leerProfesores.html", {"mensaje":"Profesor editado correctamente", "profesores": profesores, "imagen":obtenerAvatar(request)})
    else:
        formulario= ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "antiguedad":profesor.antiguedad,"email":profesor.email,"materia":profesor.materia, "imagen":obtenerAvatar(request)})
    
   
    return render (request, "editarProfesor.html", {"form":formulario, "profesor":profesor, "imagen":obtenerAvatar(request)})
    
    
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
    return render (request, "editarTrabajo.html", {"form":formulario, "trabajo":trabajo, "imagen":obtenerAvatar(request)})
    
    
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
                return render (request, "inicio.html", {"mensaje": f"Bienvenid@ Profe {usuario}", "imagen":obtenerAvatar(request) })
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

@login_required
def editarUsuario(request):
    usuario= request.user
    if request.method=="POST":
        form=UserEditForm (request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render (request, "inicio.html",{"mensaje":"Perfil editado correctamente", "imagen":obtenerAvatar(request)})
        else:
            return render (request, "editarUsuario.html",{"mensaje":"Error al editar el usuario", "imagen":obtenerAvatar(request)})
            
    else:
        form=UserEditForm(instance=usuario)
        return render (request, "editarUsuario.html",{"form":form,})








#------------REVISAR PARA QUE INICIE DIRECTAMENTE, SIN PONER APPFINAL
def vistaInicio(request):
  return render(request, 'inicio.html')


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render (request, "inicio.html", {"mensaje":"Avatar creado correctamente"})
        else:
            return render(request, "agregarAvatar.html", {"formulario":form, "usuario": request.user, "imagen":obtenerAvatar(request)})    
    else:
        form=AvatarForm()
        return render(request, "agregarAvatar.html", {'formulario':form, "usuario":request.user, "imagen":obtenerAvatar(request)})


   
def sobrenosotros(request):
    
    return render (request, "sobrenosotros.html", {"imagen":obtenerAvatar(request)})


#@login_required
#def chat(request):
#    users = User.objects.all()
#    return render(request, 'chat.html', {'users': users})

#@login_required
#def chat(request):
#    user_messages = Message.objects.filter(recipient=request.user)
#    users = User.objects.all()
#    return render(request, 'chat.html', {'users': users, 'user_messages': user_messages})


@login_required
def chat(request):
    user_messages = Message.objects.filter(recipient=request.user)
    messages = [{'sender': message.sender.username, 'content': message.content} for message in user_messages]
    users = User.objects.all()
    return render(request, 'chat.html', {'users': users, 'messages': messages})

def urlDisponibles(request):
    
    return render (request, "urlDisponibles.html", {"imagen":obtenerAvatar(request)})


def en_proceso(request):
    return render (request, 'en_proceso.html')


def errorinterno(request):
    return render (request, 'errorinterno.html')

def custom_404(request, exception=None):
    return redirect('en_proceso')


def custom_500(request, exception=None):
    return redirect('errorinterno')
