# backend_app/urls.py
from django.contrib import admin           # ✅ import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),       # ✅ add the admin route
    path("login/", views.login_view, name="login"),
    path("posts/", views.posts_view, name="posts"),
]
