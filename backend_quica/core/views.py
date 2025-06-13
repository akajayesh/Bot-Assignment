from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from core.task import send_wlc_email

@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "This is a public endpoint."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": f"Hello, {request.user.username}. This is a protected endpoint."})

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists."}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)

    # Celery async email
    send_wlc_email.delay(user.email)

    return Response({"message": "User registered successfully."})

def home(request):
    return render(request, 'index.html')