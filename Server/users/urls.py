from .views import *
from django.urls import path

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    path("update-user/", update_user, name="update_user"),
    path("get-user/", get_user_data, name="get_user_data"),
    path("csrf/", obtain_csrftoken, name="obtain_csrftoken"),
]
