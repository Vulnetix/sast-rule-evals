# Django settings for evaluation project
SECRET_KEY = "django-insecure-evaluation-key"

# VNX-PY-006: DEBUG=True in Django settings
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
]
