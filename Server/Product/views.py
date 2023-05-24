from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from Users.models import CustomUser
from Category.models import Category
from utils.get_user_id import get_user_by_sessionid


class ProductListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "page_size": self.page_size,
                "results": data,
            }
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def product_list(request):
    paginator = ProductListPagination()
    products = Product.objects.all()
    sort_by = request.GET.get("sort_by", "-id")
    products = products.order_by(sort_by)

    paginated_products = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(paginated_products, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def product_create(request):
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)
    user = CustomUser.objects.get(pk=user_obj.id)
    if user.is_dealer != True:
        Response(status=status.HTTP_401_UNAUTHORIZED)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny])
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(["PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def product_adjust(request, pk):
    product = get_object_or_404(Product, pk=pk)
    try:
        user_obj = get_user_by_sessionid(request.COOKIES.get("sessionid"))
    except Exception as e:
        return Response(status=status.HTTP_403_FORBIDDEN)

    user = get_object_or_404(CustomUser, pk=user_obj.id)

    if request.method == "PUT" or request.method == "DELETE":
        if user.is_dealer != False:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "PUT":
        # Make sure category exist
        category_list = request.data.get(
            "category", [category.id for category in product.category.all()]
        )
        categories = [
            get_object_or_404(Category, pk=category_id) for category_id in category_list
        ]
        get_object_or_404(CustomUser, pk=request.data.get("dealer", product.dealer.id))

        data = {
            "name": request.data.get("name", product.name),
            "description": request.data.get("description", product.description),
            "price": request.data.get("price", product.price),
            "discount": request.data.get("discount", product.discount),
            "category": [cat.id for cat in categories],
            "dealer": request.data.get("dealer", product.dealer.id),
        }

        serializer = ProductSerializer(
            product,
            data=data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
