#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn SongScrapper .wsgi:application --bind 0.0.0.0:$PORT
