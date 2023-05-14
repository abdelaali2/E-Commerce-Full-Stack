from django.urls import path
from .views import *


urlpatterns = [
    path('shipments/', ShipmentListCreateAPIView.as_view(), name='shipment-list'),
    path('shipments/<int:pk>/', ShipmentRetrieveUpdateDestroyAPIView.as_view(), name='shipment-detail'),
]