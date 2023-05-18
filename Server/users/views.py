from django import forms
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    print("login view")
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = JsonResponse(
            {"Success": True, "sessionid": request.session.session_key}
        )
        return response
    else:
        return JsonResponse({"Success": False, "error": form.errors})


@api_view(["POST", "OPTIONS"])
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return Response(
            {"detail": "Logged out successfully."}, status=status.HTTP_200_OK
        )
    elif request.method == "OPTIONS":
        response = Response()
        response["allow"] = "POST, OPTIONS"
        return response


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    print("Registering")
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        response = JsonResponse(
            {"Success": True, "sessionid": request.session.session_key}
        )
        return response
    else:
        return JsonResponse({"Success": False, "errors": form.errors})
