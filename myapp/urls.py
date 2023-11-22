from myapp import views
from django.urls import path
from .views import guardar_coordenadas


urlpatterns = [

    path('', views.index, name='index'),
    path('mapas/',views.mapas, name="mapas"),
    path('mapa1/', views.mapa1, name='mapa1'),  # Ruta para mapa1
    path('mapa2/', views.mapa2, name='mapa2'),  # Ruta para mapa2
    path('mapa3/',views.mapa3, name='mapa3' ),  # Ruta para mapa3
    path('mapa4/',views.mapa4, name='mapa4' ),  # Ruta para mapa4
    path('mapa5/',views.mapa5, name='mapa5' ),  # Ruta para mapa5
    path('mapa6/',views.mapa6, name='mapa6' ),  # Ruta para mapa de prueba 1
    path('mapa7/',views.mapa7, name='mapa7' ),  # Ruta para mapa de prueba 2
    path('mapa8/',views.mapa8, name='mapa8' ),  # Ruta para mapa de prueba 3

    path('mas informacion/', views.mas_informacion, name= "mas_informacion"),
    path('mapa1/', views.guardar_coordenadas, name='guardar_coordenadas'),
    path('pruebas/',views.pruebas, name='pruebas'),
    path('loadScreen/', views.loadScreen, name='loadscreen'),
    path('guardar_coordenadas/', views.guardar_coordenadas, name='guardar_coordenadas')
]