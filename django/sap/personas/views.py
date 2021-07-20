
from django.shortcuts import get_object_or_404, redirect, render
from personas.models import Persona
# from django.forms import modelform_factory
from personas.forms import PersonaForm
# Create your views here.
def detalle(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle.html', {'persona':persona})

# PersonaForm = modelform_factory(Persona, exclude=[])

def newPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = PersonaForm()
    
    return render(request, 'new.html', {'formaPersona': formaPersona})

def editPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = PersonaForm(instance = persona)
    
    return render(request, 'edit.html', {'formaPersona': formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')