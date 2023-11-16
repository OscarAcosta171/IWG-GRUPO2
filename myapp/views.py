from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MarkerForm
from .models import Marker
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):                         #Pagina principal
    return render(request, 'index.html')

def mapas(request):                         #Opcion mapas
    return render(request, "mapas.html")

def mas_informacion(request):               #Mas informacion de reciclaje
    return render(request, 'mas_informacion.html')

def mapa1(request):                         # mapa 1
    return render(request, 'mapa1.html')

def mapa2(request):                          #mapa2
    return render(request, 'mapa2.html')

def mapa3(request):                          #mapa3
    return render(request, 'mapa3.html')

def mapa4(request):                          #mapa4
    return render(request, 'mapa4.html')

def pruebas(request):
    return render(request, 'pruebas.html')

def loadScreen(request):
    return render(request, 'loadScreen.html')

@csrf_exempt
def guardar_coordenadas(request):   
    if request.method == 'POST':
        x = request.POST.get('x')
        y = request.POST.get('y')
        Tipo = request.POST.get('Tipo')
        markerColor = request.POST.get('markerColor')
        mapa = request.POST.get('mapa')

        Marker.objects.create(x =x, y = y, Tipo = Tipo, color = markerColor, mapa = mapa)
        return JsonResponse({'message': 'Marker saved successfully'})

    return JsonResponse({'message': 'Invalid request'})
