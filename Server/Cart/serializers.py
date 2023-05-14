from rest_framework import serializers
from User.serializers import UserSerializer
from Product.serializers import ProductSerializer
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"
