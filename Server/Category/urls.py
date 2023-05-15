from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='Category-list'),
    path('categories/<int:pk>/', views.category_detail, name='Category-detail'),
]