from rest_framework import serializers

from apps.hardware.models import Station


class StationSerializer(serializers.HyperlinkedModelSerializer):
    is_battery_available = serializers.BooleanField(required=False, read_only=True)

    class Meta:
        model = Station
        fields = '__all__'
        read_only_fields = ['id', 'is_battery_available']
    