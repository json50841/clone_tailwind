# backend_app/views.py

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from functools import wraps

from data_analy.dataanaly import run_analysis_wrapper


# --------------------------
# Helper: check if any admin exists
# --------------------------
def any_admin_exists():
    """Returns True if there is at least one superuser (admin) in the system."""
    return User.objects.filter(is_superuser=True).exists()


# --------------------------
# Decorator: require at least one admin
# --------------------------
def require_admin_exists(func):
    """Decorator to check if at least one admin exists before executing the view."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if not any_admin_exists():
            return Response({"detail": "没有管理员，无法访问文章"}, status=status.HTTP_403_FORBIDDEN)
        return func(*args, **kwargs)
    return wrapper


# --------------------------
# Public API: check if admin exists
# --------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def check_admin_exists(request):
    """Public endpoint: check if there is at least one admin in the system."""
    return Response({"admin_exists": any_admin_exists()})


# --------------------------
# Login API
# --------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def login_post(request):
    """Public endpoint: login with username and password, return token."""
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"detail": "用户名或密码错误"}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"message": "登录成功", "token": token.key})


# --------------------------
# Protected API: root
# --------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@require_admin_exists
def root(request):
    """Protected endpoint: returns analysis result."""
    analysis_result = run_analysis_wrapper()
    return Response({"message": f"Hello, {request.user.username}! {analysis_result}"})


# --------------------------
# Protected API: get posts
# --------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@require_admin_exists
def get_posts(request):
    """Protected endpoint: returns a list of posts."""
    posts = [
        {"id": 1, "title": "第一篇文章", "summary": "这是第一篇文章的摘要"},
        {"id": 2, "title": "第二篇文章", "summary": "这是第二篇文章的摘要"},
    ]
    return Response(posts)
