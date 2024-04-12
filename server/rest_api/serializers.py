from rest_framework import serializers
from .models import LatLongs


class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLongs
        fields = ["lattitude", "longitude", "distance"]
