from django.db import models

# Create your models here.
class Marker(models.Model):
    map_name = models.CharField(max_length=255)
    x = models.FloatField()
    y = models.FloatField()
    description = models.TextField()