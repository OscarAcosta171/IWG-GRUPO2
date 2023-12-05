from django.shortcuts import render, get_object_or_404
import json
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

def mapa5(request):                          #mapa5
    return render(request, 'mapa5.html')

def mapa6(request):                          #mapa de prueba 1
    return render(request, 'mapa6.html')

def mapa7(request):                          #mapa de prueba 2
    return render(request, 'mapa7.html')

def mapa8(request):                          #mapa de prueba 3
    return render(request, 'mapa8.html')

def pruebas(request):
    return render(request, 'pruebas.html')

def loadScreen(request):
    return render(request, 'loadScreen.html')



def load_markers(request, mapa):
    markers = Marker.objects.filter(mapa = mapa).values('x_coordinate', 'y_coordinate', 'color')
    return render(request, 'mapa6', {'markers': markers})

@csrf_exempt
def save_request(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        form = MarkerForm(data)

        if form.is_valid():
            mapa = form.cleaned_data['mapa']
            x_coordinate = form.cleaned_data['x_coordinate']
            y_coordinate = form.cleaned_data['y_coordinate']
            tipo = form.cleaned_data['tipo']


            # Save data to the database
            Marker.objects.create(mapa = mapa, x_coordinate = x_coordinate, y_coordinate = y_coordinate, tipo = tipo)

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()})

    return JsonResponse({'status': 'error'})

@csrf_exempt
def remove_marker(request, latitude, longitude):
    marker = get_object_or_404(Marker, latitude=latitude, longitude=longitude)
    marker.delete()
    return JsonResponse({'status': 'success'})