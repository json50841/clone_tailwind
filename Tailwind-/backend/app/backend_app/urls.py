from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("posts/", views.posts_view, name="posts"),  # <-- use /posts/
]
