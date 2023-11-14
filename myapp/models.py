from django.db import models

# Create your models here.
class Marker(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    tipo = models.TextField()
    mapa = models.FloatField()


