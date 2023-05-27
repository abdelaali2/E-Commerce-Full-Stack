from rest_framework import serializers
from .models import Cart, CartItem
from Product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'updated_at']
        
        