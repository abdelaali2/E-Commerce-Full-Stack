from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        models = Product
        fields = "__all__"

