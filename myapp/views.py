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

def guardar_marcadores(request):
    if request.method == 'POST':
        # Obtén los datos de los marcadores de la solicitud
        marcadores = request.POST.getlist('marcadores[]')  # Ajusta el nombre según lo que estés enviando
        # Limpia la base de datos para eliminar los marcadores antiguos
        Marker.objects.all().delete()
        # Guarda los nuevos marcadores en la base de datos
        for marcador in marcadores:
            datos = marcador.split(',')
            if len(datos) == 4:
                map_name, x, y, descripcion = datos
                Marker.objects.create(map_name=map_name, x=x, y=y, description=descripcion)
        # Redirige a la página de éxito o a donde desees
        return redirect('nombre_de_la_vista')
    else:
        return render(request, 'myapp/mapa4.html')