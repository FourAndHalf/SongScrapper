import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpotifyDownloader.settings")

app = Celery("SpotifyDownloader")