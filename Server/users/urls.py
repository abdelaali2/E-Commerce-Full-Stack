from django.urls import path
from .views import login_view, logout_user, register_user

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register_user, name='register_user'),
]