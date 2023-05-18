from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.Category_list, name='Category-list'),
    path('categories/<int:pk>/', views.Category_detail, name='Category-detail'),
]