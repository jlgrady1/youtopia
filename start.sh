#!/bin/sh

echo "Collecting static files"
python manage.py  collectstatic --no-input
python manage.py migrate
# celery
echo "Starting Gunicorn."
if [ $DEBUG == 'True' ]; then
    python manage.py runserver 0.0.0.0:8000
else
    exec gunicorn youtopia.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 3
fi
