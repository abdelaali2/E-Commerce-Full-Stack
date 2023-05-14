from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/", UserList.as_view()),
    path("create/", CreateUserView.as_view(), name="create_user"),
    path("<int:pk>/edit/", EditUserView.as_view(), name="edit_user"),
]
