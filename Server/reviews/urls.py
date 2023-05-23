from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>/', views.review_details, name='review-details'),
    path('user/<int:pk>/', views.user_review, name='user-review'),
    # path('product/<int:pk>', views.product_review, name='product-review'),
]