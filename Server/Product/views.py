from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "price"]


class ProductListPerCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        queryset = Product.objects.filter(Category__name__iexact=category_name)
        return queryset

