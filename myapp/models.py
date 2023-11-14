from django.db import models

# Create your models here.
class Marker(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    Tipo = models.TextField()
    mapa = models.CharField(max_length=255)