from django.shortcuts import render, get_object_or_404
import json
from django.http import HttpResponse
from .forms import MarkerForm
from .models import Marker
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

# Create your views here.
def index(request):                         #Pagina principal
    return render(request, 'index.html')

def mapas(request):                         #Opcion mapas
    return render(request, "mapas.html")

def mas_informacion(request):               #Mas informacion de reciclaje
    return render(request, 'mas_informacion.html')

def mapa1(request):                         # mapa 1
    markers = Marker.objects.filter(mapa='mapa1')
    markers_json = serialize('json', markers)
    markers_data = json.loads(markers_json)
    return render(request, 'mapa1.html', {'markers_json': json.dumps(markers_data)})

def mapa2(request):                          #mapa2
    markers = Marker.objects.filter(mapa='mapa2')
    markers_json = serialize('json', markers)
    markers_data = json.loads(markers_json)
    return render(request, 'mapa2.html', {'markers_json': json.dumps(markers_data)})
def mapa3(request):                          #mapa3
    markers = Marker.objects.filter(mapa='mapa3')
    markers_json = serialize('json', markers)
    markers_data = json.loads(markers_json)
    return render(request, 'mapa3.html', {'markers_json': json.dumps(markers_data)})
def mapa4(request):                          #mapa4
    markers = Marker.objects.filter(mapa='mapa4')
    markers_json = serialize('json', markers)
    markers_data = json.loads(markers_json)
    return render(request, 'mapa4.html', {'markers_json': json.dumps(markers_data)})

def mapa5(request):                          #mapa5
    markers = Marker.objects.filter(mapa='mapa5')
    markers_json = serialize('json', markers)
    markers_data = json.loads(markers_json)
    return render(request, 'mapa5.html', {'markers_json': json.dumps(markers_data)})

def mapa6(request):                          #mapa de prueba 1
    markers = Marker.objects.filter(mapa='mapa6')
    markers_json = serialize('json', markers)
    markers_data = json.loads(markers_json)
    return render(request, 'mapa6.html', {'markers_json': json.dumps(markers_data)})

def mapa7(request):                          #mapa de prueba 2
    markers = Marker.objects.filter(mapa='mapa7')
    markers_json = serialize('json', markers)
    markers_data = json.loads(markers_json)
    return render(request, 'mapa7.html', {'markers_json': json.dumps(markers_data)})

def mapa8(request):                          #mapa de prueba 3
    markers = Marker.objects.filter(mapa='mapa8')
    markers_json = serialize('json', markers)
    markers_data = json.loads(markers_json)
    return render(request, 'mapa8.html', {'markers_json': json.dumps(markers_data)})

def pruebas(request):
    return render(request, 'pruebas.html')

def loadScreen(request):
    return render(request, 'loadScreen.html')

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
def delete_marker(request, marker_id):
    marker = get_object_or_404(Marker, pk=marker_id)
    marker.delete()
    return JsonResponse({'message': 'Marker deleted successfully'})
