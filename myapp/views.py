from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def title(request):
    return HttpResponse("USM ECO GUIDE")
def mapas(request):
    return HttpResponse("Mapas")