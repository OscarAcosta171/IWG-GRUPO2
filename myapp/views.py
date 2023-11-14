from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MarkerForm
from .models import Marker
from django.http import JsonResponse

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
def agregar_marcador(request):
    if request.method == 'POST':
        form = MarkerForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir o realizar otras acciones después de guardar
            return redirect('nombre_de_la_vista')
    else:
        form = MarkerForm()
    return render(request, 'template.html', {'form': form})

def guardar_coordenadas(request):
    if request.method == 'POST':
        x = request.POST.get('x')
        y = request.POST.get('y')
        Tipo = request.POST.get('Tipo')
        mapa = request.POST.get('mapa')

        print(f'x: {x}, y: {y}, Tipo: {Tipo}, mapa: {mapa}')

        Marker.objects.create(
            x = float(x),
            y = float(y),
            Tipo = Tipo,
            mapa = int(mapa)
        )
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})