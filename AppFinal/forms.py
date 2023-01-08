from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


    
class MateriaForm (forms.Form):
    materia = [
        ('Matemáticas', 'Matemáticas'),
        ('Física', 'Física'),
        ('Química', 'Química'),
        ('Biología', 'Biología'),
        ('Historia', 'Historia'),
        ('Geografía', 'Geografía'),
    ]
    nombre = forms.ChoiceField(choices=materia)


class ProfesorForm (forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    antiguedad=forms.IntegerField()
    email = forms.EmailField()
    materia = forms.CharField(max_length=20)
    
    
class TrabajoForm (forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField()
    archivo = forms.FileField()
    #datos = models.DateTimeField(auto_now=True)
    #profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    profesor = forms.CharField(max_length=200)
    materia = forms.CharField()

#class TrabajoForm(forms.Form):
#    class Meta:
#        model = TrabajoPractico
#        fields = ['titulo', 'descripcion', 'archivo', 'profesor', 'materia']

class RegistroUsuarioForm(UserCreationForm):
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Reingrese Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Reingrese Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ["first_name","last_name","username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
        
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")
