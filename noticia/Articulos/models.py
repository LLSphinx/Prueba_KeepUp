import imp
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Entrada(models.Model):  # ---> Se crea la clase 
    nombre =   models.CharField(max_length=100)
    contenido = models.TextField(max_length=700)
    imagen = models.URLField()
    viewmore = models.URLField()
    autor = models.CharField(max_length=50 )


# ---> Se añade el parametro str para mostrar el nombre en las entradas 
    def __str__(self):
        return self.nombre  