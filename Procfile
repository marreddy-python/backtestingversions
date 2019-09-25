web: gunicorn --bind 0.0.0.0:$PORT run:app
worker: celery -A celery_task worker --loglevel=info 
beat: celery -A celery_task beat --loglevel=info