from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    print("Registering")
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        response = JsonResponse(
            {"status": "success", "token": request.session.session_key}
        )
        return response
    else:
        return JsonResponse({"status": "error", "errors": form.errors})


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    print("login view")
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = JsonResponse(
            {"status": "success", "token": request.session.session_key}
        )
        return response
    else:
        return JsonResponse({"status": "error", "errors": form.errors})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    response = JsonResponse({"status": "success"})
    response.delete_cookie("sessionid")
    return response
