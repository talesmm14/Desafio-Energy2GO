from rest_framework import viewsets

from apps.hardware.models import Station
from apps.hardware.serializers import StationSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
