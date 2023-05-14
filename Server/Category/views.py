from django.shortcuts import render
from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from Product.serializers import ProductSerializer
from Product.models import Product

# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryProductsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Product.objects.filter(category__name__iexact=category_name)