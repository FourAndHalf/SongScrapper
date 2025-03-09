#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn songscrapper .wsgi:application --bind 0.0.0.0:$PORT
