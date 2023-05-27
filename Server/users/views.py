import base64
from django.http import HttpResponse, JsonResponse
from django.middleware import csrf
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.sessions.models import Session
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from .serializers import CustomUserCreationForm


@api_view(["GET"])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def obtain_csrftoken(request):
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
        response["Access-Control-Allow-Credentials"] = "true"
        return response
    else:
        return JsonResponse({"error": form.errors})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    print("request", request)
    print("session", request.session)
    logout(request)
    response = HttpResponse(status=204)
    response["Access-Control-Allow-Credentials"] = "true"
    response.delete_cookie("sessionid")
    print("response.cookies before", response.cookies)
    print("response.cookies after", response.cookies)
    return response


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    form = CustomUserCreationForm(request.POST, request.FILES)
    print("request.FILES", request.FILES)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return JsonResponse({}, status=204)
    else:
        print("form.errors", form.errors)
        return JsonResponse({"errors": form.errors}, status=400)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
        form.save()
        return JsonResponse({}, status=204)
    else:
        return JsonResponse({"errors": form.errors}, status=400)


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
    if user.profile_picture:
        with open(user.profile_picture.path, "rb") as f:
            encoded_picture = base64.b64encode(f.read()).decode("utf-8")
    user_profile = {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "last_name": user.last_name,
        "first_name": user.first_name,
        "joined_at": user.date_joined,
        "is_dealer": user.is_dealer,
        "profile_picture": encoded_picture,
    }
    return JsonResponse(user_profile)
