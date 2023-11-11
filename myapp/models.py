from django.db import models

# Create your models here.
class Marker(models.Model):
    map_id = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    tipo = models.TextField()