from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.models import Token


@api_view(["POST", "OPTIONS"])
def login_user(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token = Token.objects.get_or_create(user=user)
            response = Response({"success": True}, status=status.HTTP_200_OK)
            response.set_cookie(
                key="session_token",
                value=token[0],
                max_age=settings.SESSION_COOKIE_AGE,
                httponly=True,
                secure=True,
                path="/",
                samesite="Lax",
            )
            return response
        else:
            return Response(
                {"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST
            )
    # elif request.method == "OPTIONS":
    #     response = Response()
    #     response["allow"] = "POST, OPTIONS"
    #     return response


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


@api_view(["POST", "OPTIONS"])
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return Response(
                {"detail": "Registration successful."}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"detail": "Registration failed.", "error": form.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
    elif request.method == "OPTIONS":
        response = Response()
        response["allow"] = "POST, OPTIONS"
        return response
    else:
        form = UserCreationForm()
    return Response({"form": form}, status=status.HTTP_200_OK)
