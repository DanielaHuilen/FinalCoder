from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Profesores (models.Model):
    nombre= models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    antiguedad=models.IntegerField()
    email = models.EmailField(unique=True)
    #materia = models.ManyToManyField(Materia)
    materia=models.CharField(max_length=50, default="Desconocido")
    
    def __str__ (self):
        return f"Docente: {self.apellido} {self.nombre}, docente de {self.materia} "
    
    
class TrabajoPractico(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo = models.FileField()
    #datos = models.DateTimeField(auto_now_add=True)
    #profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    profesor=models.CharField(max_length=70)
    materia = models.CharField(max_length=50, default="Desconocido")

    def __str__(self):
        return self.titulo + " " + self.descripcion 
    
class Avatar (models.Model):
    imagen=models.ImageField(upload_to="avatares")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} . {self.imagen}"
        
