from __future__ import absolute_import, unicode_literals
from flask import Flask
from celery import Celery
from celery_config import make_celery,create_db,check_database
from datetime import timedelta
from celery.schedules import crontab


app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://h:p6626f06147f8c0f4f0acff655ad7ef9c50cf5715d11deeb9994ea6a92814315c@ec2-34-238-13-119.compute-1.amazonaws.com:30069',
    # CELERY_RESULT_BACKEND='redis://localhost:6379/0',
    CELERYBEAT_SCHEDULE = {
        'periodic_task-every-minute': {
            'task': 'periodic_task',
            'schedule': crontab(minute="18",hour="15" ,day_of_week="mon,tue,wed,thu,fri")
        }}
)

celery = make_celery(app)

db = create_db(app)

from models_celery.tables import price_data,Strategy_features,Market_data_audit_log

check_database(db)

from startup import main

@celery.task(name ="periodic_task")

def send_async_email():
    
    main() 


