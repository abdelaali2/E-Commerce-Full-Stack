from django.urls import path
from . import views

urlpatterns = [
    path("", views.order, name="order"),
    path("delete/<int:pk>/", views.delete_order, name="delete_order"),
    path("create/", views.create_order, name="create_order"),
]
