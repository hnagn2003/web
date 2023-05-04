"""
Django settings for BookRecSystem project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "RANDOM_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get("DEBUG", True)) == "True"

# Check if production environment
PROD_ENV = str(os.environ.get("PROD_ENV", False)) == "True"

ALLOWED_HOSTS = [
    "kitabe-app.herokuapp.com",
    "kitabe.up.railway.app",
    "127.0.0.1",
    "localhost",
    "web-production-ac16.up.railway.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://kitabe-app.herokuapp.com",
    "https://kitabe.up.railway.app",
    "https://web-production-ac16.up.railway.app",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # disable django static file handling during development as well
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "mainapp",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "BookRecSystem.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # allauth
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "BookRecSystem.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if PROD_ENV:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("PGDATABASE"),
            "USER": os.environ.get("PGUSER"),
            "PASSWORD": os.environ.get("PGPASSWORD"),
            "HOST": os.environ.get("PGHOST"),
            "PORT": os.environ.get("PGPORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Calcutta"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# url/placeholder path at which static files are served
STATIC_URL = "/static/"
# other folders to look for static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Deployment
# Directory where collectstatic will collect the static files for deployment
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


AUTHENICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    # allauth
    "allauth.account.auth_backends.AuthenicationBackend",
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get("KITABE_AUTH_ID"),
            "secret": os.environ.get("KITABE_AUTH_SECRET"),
            "key": "",
        }
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# media files
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"

# simple mail transfer protocal
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("KITABE_EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get("KITABE_PASS")

# Alluth Settings
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGOUT_ON_GET = True

if not DEBUG:
    # access via https in production
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}
