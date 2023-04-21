from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Paleta(models.Model):
    modelo=models.CharField(max_length=40)
    marca=models.CharField(max_length=20)
    descripcion=RichTextField()
    stock=models.IntegerField()
    fecha_de_carga=models.DateField()
    
    def __str__(self):
        return f"{self.modelo} - {self.marca}"