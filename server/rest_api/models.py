from django.db import models


class LatLongs(models.Model):
    lattitude = models.FloatField()
    longitude = models.FloatField()
    distance = models.FloatField()
