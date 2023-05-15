from rest_framework import serializers
from .models import Cart, CartItem
from Product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    Product = ProductSerializer()
    
    class Meta:
        model = CartItem
        fields = ['id', 'Product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'updated_at', 'items']