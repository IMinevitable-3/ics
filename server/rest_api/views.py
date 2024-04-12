from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import LatLongSerializer
from .models import LatLongs
from .logic import grid


class GetDistanceAndLoc(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LatLongSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            center_lat = instance.lattitude
            center_lon = instance.longitude
            distance = instance.distance
            grid_data = grid(center_lat, center_lon, distance)
            return Response(grid_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        latlong = LatLongs.objects.all()
        serializer = LatLongSerializer(latlong, many=True)
        return Response(serializer.data)
