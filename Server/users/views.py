import base64
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.middleware import csrf
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import login, logout, get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
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
        return JsonResponse({"error": form.errors}, status=400)


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
    print("request.POST", request.POST, request.user)
    if form.is_valid():
        form.save()
        return JsonResponse({}, status=204)
    else:
        return JsonResponse({"errors": form.errors}, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    print("/*/*/*/*/*/*/*/*///////*****", request)
    print("request=============>", request.user)
    # Extract the session ID from the request
    sessionid = request.COOKIES.get("sessionid")

    # # Create a session store using the session ID
    # session_store = SessionStore(session_key=sessionid)

    # # Decode the session data to get the user ID
    # user_id = session_store.get("_auth_user_id")

    # # Use the user ID to get the user object
    # User = get_user_model()
    # user = User.objects.get(pk=user_id)

    # # Do something with the user object
    # # ...
    # print("session==========>", user)
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
    encoded_picture = None
    # if user.profile_picture:
    #     with open(user.profile_picture.path, "rb") as f:
    #         encoded_picture = base64.b64encode(f.read()).decode("utf-8")
    # else:
    #     default_profile_picture = None
    #     if user.gender == "Male":
    #         default_profile_picture = os.path.join(
    #             settings.BASE_DIR, "media", "default_male_profile_picture.png"
    #         )
    #     elif user.gender == "Female":
    #         default_profile_picture = os.path.join(
    #             settings.BASE_DIR, "media", "default_female_profile_picture.png"
    #         )
    #     print("Using default profile Picture: ", default_profile_picture)
    #     with open(default_profile_picture, "rb") as f:
    #         encoded_picture = base64.b64encode(f.read()).decode("utf-8")

    print(
        "===================>",
        os.path.join(settings.BASE_DIR, "media", "default_male_profile_picture.png"),
    )
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
