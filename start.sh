#!/bin/sh

echo "Starting Gunicorn."
exec gunicorn youtopia.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
