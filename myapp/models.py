from django.db import models

# Create your models here.
class Marker(models.Model):
    mapa = models.TextField()
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    tipo = models.TextField()
