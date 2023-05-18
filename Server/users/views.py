from django import forms
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.sessions.models import Session


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



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    response = JsonResponse({"Success": True})
    response.delete_cookie("sessionid")
    return response




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

@api_view(["GET"])
@permission_classes([AllowAny])
def get_user_data(request):
    print (request)
    sessionid = request.GET.get("sessionid")

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
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "Invalid user ID"}, status=400)

    # Return the user data as a JSON response
    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
        # Add any additional user data you want to include
    }
    return JsonResponse(user_data)
