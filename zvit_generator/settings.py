from pathlib import Path


#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Безопасность
SECRET_KEY = "replace-me-with-a-secure-key"
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Приложения
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "zvit_app",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Основной маршрутизатор URL
ROOT_URLCONF = "zvit_generator.urls"

# Настройки шаблонов
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "zvit_app" / "templates"],  # Папка с шаблонами приложения
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = "zvit_generator.wsgi.application"

# База данных
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Проверки паролей (в dev можно отключить)
AUTH_PASSWORD_VALIDATORS = []

# Локализация
LANGUAGE_CODE = "uk-ua"
TIME_ZONE = "Europe/Kyiv"
USE_I18N = True
USE_TZ = True

# ⚙️ Статика — важно для Bootstrap, JS и CSS
STATIC_URL = "/static/"

# Добавляем путь к папке, где будут лежать Bootstrap, jQuery, Icons, Datepicker
STATICFILES_DIRS = [
    BASE_DIR / "zvit_app" / "static",
]

# Авто-поле по умолчанию
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Куда собирать статические файлы (Bootstrap, JS, CSS и т.п.)
STATIC_ROOT = BASE_DIR / "staticfiles"





 

#  DEBUG = False  # для продакшн

ALLOWED_HOSTS = [
    'zvit-generator-h2f7fvhfd3fwawbv.westeurope-01.azurewebsites.net',
    'localhost',
    '127.0.0.1',
]

CSRF_TRUSTED_ORIGINS = [
    'https://zvit-generator-h2f7fvhfd3fwawbv.westeurope-01.azurewebsites.net',
]
