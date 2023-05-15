from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='Product-list'),
    path('products/<int:pk>/', views.product_detail, name='Product-detail'),
]