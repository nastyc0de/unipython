from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')
def despedirse(request):
    return HttpResponse('Despedida')
def contactar(request):
    fono = '43434312'
    return HttpResponse(f'Contactanos en: {fono}')