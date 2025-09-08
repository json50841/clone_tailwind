from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

POSTS = [
    {"id": 1, "title": "第一篇文章", "summary": "这是第一篇文章的摘要"},
    {"id": 2, "title": "第二篇文章", "summary": "这是第二篇文章的摘要"},
]

# Login API
@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "用户名或密码错误"}, status=401)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"message": "登录成功", "token": token.key})

# Get Posts API
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def posts_view(request):
    return Response(POSTS)
