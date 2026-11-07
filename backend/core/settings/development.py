import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv


# Local convenience only. Production never loads this file.
load_dotenv(Path(__file__).resolve().parents[2] / '.env')

from .base import *  # noqa: E402,F403


SECRET_KEY = 'django-insecure-development-only-mundo-aplv'
DEBUG = True

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        'DJANGO_ALLOWED_HOSTS',
        'localhost,127.0.0.1,[::1],testserver',
    ).split(',')
    if host.strip()
]

database_url = os.getenv('DATABASE_URL', '').strip()
DATABASES = {
    'default': dj_database_url.parse(
        database_url or f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        conn_health_checks=True,
    )
}
