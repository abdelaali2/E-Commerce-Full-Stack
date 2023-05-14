from django.urls import path
from .views import *

urlpatterns = [
    path("", CartListCreate.as_view()),

]
