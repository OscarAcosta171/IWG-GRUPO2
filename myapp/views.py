from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MarkerForm
from .models import Marker

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

def add_marker(request):
    if request.method == 'POST':
        form = MarkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mapa1')  # Redirige a la página del mapa correspondiente
    else:
        form = MarkerForm()
    return render(request, 'add_marker.html', {'form': form})

def mapa1(request):
    markers = Marker.objects.filter(map_name="Mapa 1")
    return render(request, 'mapa1.html', {'markers': markers})
