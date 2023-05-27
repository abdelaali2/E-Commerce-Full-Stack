from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="Product-list"),
    path("<int:pk>/", views.product_details, name="Product-detail"),
    path("add/", views.product_create, name="Product-create"),
    path("adjust/<int:pk>/", views.product_adjust, name="Product-adjust"),
]
