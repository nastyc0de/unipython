
from django.shortcuts import get_object_or_404, render
from personas.models import Persona
# Create your views here.
def detalle(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle.html', {'persona':persona})