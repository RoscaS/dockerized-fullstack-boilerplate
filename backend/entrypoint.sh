#!/bin/bash
python manage.py migrate

# Start Gunicorn processes
echo Starting gunicorn.
exec gunicorn app.wsgi \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --log-level=info \
    --log-file=/logs/gunicorn.log \
    --access-logfile=/logs/access.log \
    --reload
