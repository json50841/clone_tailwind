from pathlib import Path

# --------------------------
# 基本路径设置
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------
# 安全与调试
# --------------------------
SECRET_KEY = "django-insecure-)trxhnn**pn3a9sksonrd97239ez3d*y6xj7^dufg_!9bnu2nd"
DEBUG = True
ALLOWED_HOSTS = ["*"]  # 开发阶段允许所有 host

# --------------------------
# 应用列表
# --------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",          # Django REST Framework
    "rest_framework.authtoken",# DRF Token 认证
    "corsheaders",             # 跨域
    "backend_app",             # 你的 Django 应用
]

# --------------------------
# 中间件
# --------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # 必须放在最前面
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------
# URL 配置
# --------------------------
ROOT_URLCONF = "backend_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # 可以放模板文件夹
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myproject.wsgi.application"

# --------------------------
# 数据库（SQLite 开发用）
# --------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --------------------------
# 密码验证
# --------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------
# 国际化
# --------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------
# 静态文件
# --------------------------
STATIC_URL = "static/"

# 默认主键字段类型
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------
# CORS 跨域配置（开发阶段）
# --------------------------
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
CORS_ALLOW_METHODS = ["*"]

# --------------------------
# DRF 配置：启用 Token 认证
# --------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
