from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("Product.urls")),
    path("categories/", include("Category.urls")),
    path("users/", include("User.urls")),
    path("carts/", include("Cart.urls")),
    path("shipments/", include("Shipment.urls")),
    path("payments/", include("Payment.urls")),
    path("token/obtain/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
