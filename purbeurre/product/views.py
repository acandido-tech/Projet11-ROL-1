from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    message = "Bienvenue sur l'application 'product'."
    return HttpResponse(message)