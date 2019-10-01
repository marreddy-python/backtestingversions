web: gunicorn --bind 0.0.0.0:$PORT run:app -timeout 120
worker: celery -A celery_task.celery worker --loglevel=info 
beat: celery beat -A celery_task.celery --loglevel=info