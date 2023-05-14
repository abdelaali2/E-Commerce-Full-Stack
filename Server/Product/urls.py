from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductList.as_view()),
    path('<str:category_name>/', ProductListPerCategory.as_view(), name='product-list-by-category'),
]
