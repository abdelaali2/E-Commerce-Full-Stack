from django.urls import path
from . import views

urlpatterns = [
    path("edit/<int:pk>", views.edit_payment, name="edit-payment"),
]
