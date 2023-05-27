from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer
from Users.models import CustomUser
from Product.models import Product

# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def user_review(request, pk):
    reviews = get_list_or_404(Review, user=pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=200)


@api_view(["GET"])
@permission_classes([AllowAny])
def review_details(request, pk):
    review = get_object_or_404(Review, pk=pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=200)
