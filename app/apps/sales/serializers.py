from rest_framework import serializers

from apps.hardware.models import Station
from apps.sales.models import Transaction


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'description']


class TransactionSerializer(serializers.ModelSerializer):
    station = StationSerializer(read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'status']

    def get_status(self, obj):
        return obj.get_status_display()
