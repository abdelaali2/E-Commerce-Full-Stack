from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="Product-list"),
    path("<int:pk>/", views.product_detail, name="Product-detail"),
    path("add/", views.product_create, name="Product-create"),
]
