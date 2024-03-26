from rest_framework import serializers

from apps.hardware.models import Station


class StationSerializer(serializers.HyperlinkedModelSerializer):
    is_battery_available = serializers.BooleanField()

    class Meta:
        model = Station
        fields = '__all__'
        read_only_fields = ['id']
    