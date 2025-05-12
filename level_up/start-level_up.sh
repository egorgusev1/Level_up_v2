#!/bin/bash

# Run collectstatic and migrations
poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate

# Set default number of Gunicorn workers if not provided
GUNICORN_WORKERS=${GUNICORN_WORKERS:-3}

if [[ "$ENV_STATE" == "production" ]]; then
    # Corrected WSGI path: assuming wsgi.py is in level_up/level_up/
    poetry run gunicorn level_up.wsgi:application \
        --workers "$GUNICORN_WORKERS" \
        --bind 0.0.0.0:8000 \
        --forwarded-allow-ips "*"
else
    poetry run python manage.py runserver 0.0.0.0:8000
fi