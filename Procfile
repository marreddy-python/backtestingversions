web: gunicorn --bind 0.0.0.0:$PORT run:app
worker: celery -A celery_task.celery worker --loglevel=info 
beat: celery beat -A celery_task.celery --loglevel=info