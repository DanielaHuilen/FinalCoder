from django import forms
from .models import *
from django.db import models


    
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
    datos = models.DateTimeField(auto_now=True)
    profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    materia = forms.CharField()