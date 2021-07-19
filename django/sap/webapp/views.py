from django.shortcuts import render
from personas.models import Persona

# Create your views here.
def bienvenido(request):
    nroPersonas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'nro_personas':nroPersonas, 'personas': personas})