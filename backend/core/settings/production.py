import os

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403


def require_env(name):
    value = os.getenv(name, '').strip()
    if not value:
        raise ImproperlyConfigured(
            f'{name} is required when using core.settings.production.'
        )
    return value


def env_list(name, *, required=False):
    raw_value = require_env(name) if required else os.getenv(name, '')
    return [value.strip() for value in raw_value.split(',') if value.strip()]


SECRET_KEY = require_env('DJANGO_SECRET_KEY')
if (
    len(SECRET_KEY) < 50
    or len(set(SECRET_KEY)) < 5
    or SECRET_KEY.startswith('django-insecure-')
):
    raise ImproperlyConfigured(
        'DJANGO_SECRET_KEY must be a strong production key of at least 50 characters.'
    )

DEBUG = False

ALLOWED_HOSTS = env_list('DJANGO_ALLOWED_HOSTS', required=True)
if '*' in ALLOWED_HOSTS or any('://' in host or '/' in host for host in ALLOWED_HOSTS):
    raise ImproperlyConfigured(
        'DJANGO_ALLOWED_HOSTS must contain host names only and cannot use "*".'
    )

CSRF_TRUSTED_ORIGINS = env_list('DJANGO_CSRF_TRUSTED_ORIGINS')
if any(not origin.startswith('https://') for origin in CSRF_TRUSTED_ORIGINS):
    raise ImproperlyConfigured(
        'DJANGO_CSRF_TRUSTED_ORIGINS entries must be HTTPS origins.'
    )

database_url = require_env('DATABASE_URL')
try:
    DATABASES = {
        'default': dj_database_url.parse(
            database_url,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
except (TypeError, ValueError) as exc:
    raise ImproperlyConfigured('DATABASE_URL is not a valid database URL.') from exc

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Start with a reversible one-hour HSTS policy until the final domain is known.
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# Assumes the hosting proxy strips client-supplied X-Forwarded-Proto and sets it.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
