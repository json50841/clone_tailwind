from django.contrib import admin
from django.urls import path
from . import views  # your app views

urlpatterns = [
    path('admin/', admin.site.urls),       # Django admin
    path('', views.root, name='root'),     # GET /
    path('login/', views.login_post, name='login'),  # POST /login/
    path('posts/', views.get_posts, name='posts'),   # GET /posts/
]
