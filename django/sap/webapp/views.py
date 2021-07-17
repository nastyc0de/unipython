from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')