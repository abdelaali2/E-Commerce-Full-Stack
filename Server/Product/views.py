from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404


@api_view(["GET"])
@permission_classes([AllowAny])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def product_create(request):
    if not request.user.is_dealer:
        Response(status=status.HTTP_401_UNAUTHORIZED)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    if request.method == "GET":
        product = Product.objects.filter(pk=pk).first()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    
    if request.method == "PUT" or request.method == "DELETE":
        if not request.user.is_dealer:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    
    product = get_object_or_404(Product, dealer=request.user)

    
    if request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
