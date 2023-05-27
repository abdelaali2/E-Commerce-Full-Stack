from rest_framework import serializers
from payments.models import Payment


class PaymentsSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = "__all__"
