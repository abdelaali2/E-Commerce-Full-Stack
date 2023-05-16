from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
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
