from rest_framework import serializers
from shipments.models import Shipment


class ShipmentSerializer(serializers.Serializer):
    class Meta:
        model = Shipment
        fields = "__all__"
