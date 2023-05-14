from django.urls import path
from .views import *

urlpatterns = [
    path("", CategoryList.as_view()),
    path('<str:category_name>/', CategoryProductsAPIView.as_view(), name='category-products'),
]
