from django.shortcuts import render
from Articulos.models import Entrada

# Create your views here.

# Regresa una renderizacion del requiest junto el template bienvenida
def home(request):
    articulos = Entrada.objects.all()  # --> Todo lo que encuentre en modelo entrada se envia a var articulos
    return render(request,"index.html", {"articulos":articulos}) # --> Se envia al template por medio de un diccionario