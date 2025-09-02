# Register your models here.
from django.contrib import admin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# 注册 DRF 的 Token 模型，让它可以在 admin 管理
@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("key", "user", "created")
    search_fields = ("user__username", "key")
