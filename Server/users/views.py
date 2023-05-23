from django import forms
from django.http import HttpResponse, JsonResponse
from django.middleware import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.sessions.models import Session
from .models import CustomUser
from .serializers import CustomUserCreationForm


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    print("login view")
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponse(status=204)
        response["Content-Length"] = "0"
        response["Content-Type"] = "application/json"
        response.set_cookie(
            key="csrftoken",
            value=csrf.get_token(request),
            secure=True,
            max_age=86400,
        )
        response["Access-Control-Allow-Credentials"] = "true"
        return response
    else:
        return JsonResponse({"error": form.errors})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def logout_view(request):
    print("request", request)
    print("session", request.session)
    logout(request)
    response = HttpResponse(status=204)
    response["Access-Control-Allow-Credentials"] = "true"
    response.delete_cookie("sessionid")
    print("response.cookies before", response.cookies)
    response.set_cookie(
        key="csrftoken",
        value="",
        secure=True,
        max_age=0,
    )
    print("response.cookies after", response.cookies)
    return response


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    print("Registering")
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        response = HttpResponse(status=204)
        response["Content-Length"] = "0"
        response["Content-Type"] = "application/json"
        response.set_cookie(
            key="csrftoken",
            value=csrf.get_token(request),
            secure=True,
            max_age=86400,
        )
        response["Access-Control-Allow-Credentials"] = "true"
        return response
    else:
        return JsonResponse({"errors": form.errors})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    sessionid = request.COOKIES.get("sessionid")

    try:
        session = Session.objects.get(session_key=sessionid)
    except Session.DoesNotExist:
        return JsonResponse({"error": "Invalid session ID"}, status=400)

    # Extract the user ID from the session data
    user_id = session.get_decoded().get("_auth_user_id")
    if user_id is None:
        return JsonResponse(
            {"error": "Session is not associated with a user"}, status=400
        )

    # Look up the user object based on the user ID
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "Invalid user ID"}, status=400)

    # Return the user profile
    user_profile = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_dealer": user.is_dealer,
    }
    return JsonResponse(user_profile)
