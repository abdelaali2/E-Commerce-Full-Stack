from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Review
from .serializers import ReviewSerializer
from Users.models import CustomUser
from Product.models import Product
from utils.get_user_id import get_user_by_sessionid


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


@api_view(["GET"])
@permission_classes([AllowAny])
def product_review(request, pk):
    reviews = get_list_or_404(Review, product=pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=200)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def edit_review(request, pk):
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)

    review = get_object_or_404(Review, user=user_obj.id, pk=pk)
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def delete_review(request, pk):
    user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    review = get_object_or_404(Review, user=user_obj.id, pk=pk)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
