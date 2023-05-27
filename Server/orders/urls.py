from django.urls import path
from . import views

urlpatterns = [
    path("", views.order, name="order"),
    path("delete/", views.delete_order, name="delete_order"),
]
