#!/bin/bash


poetry run python manage.py collectstatic --no-input

poetry run python manage.py migrate

GUNICORN_WORKERS=${GUNICORN_WORKERS:-3}

if [[ "$ENV_STATE" == "production" ]]; then
    poetry run gunicorn level_up.wsgi. --workers $GUNICORN_WORKERS --forwarded-allow-ips "*"
else
    poetry run python manage.py runserver 0.0.0.0:8000
fi

