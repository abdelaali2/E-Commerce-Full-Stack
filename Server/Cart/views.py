from django.shortcuts import render
from .models import Cart
from rest_framework import generics
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CartListCreate(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
