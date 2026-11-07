#!/usr/bin/env sh
set -eu

export DJANGO_SETTINGS_MODULE=core.settings.production

exec gunicorn --bind "0.0.0.0:${PORT:-8000}" core.wsgi:application
