from celery import Celery
from celery.schedules import crontab
from app.config import Config

def create_celery_app(app=None):
    celery = Celery('tasks', 
                    broker=Config.CELERY_BROKER_URL,
                    backend=Config.CELERY_RESULT_BACKEND)
    
    celery.conf.update(
        task_serializer='json',
        accept_content=['json'],
        result_serializer='json',
        timezone='UTC',
        enable_utc=True,
        task_track_started=True,
        task_time_limit=900,  # 15 minutes
        broker_connection_retry_on_startup=True,
        beat_schedule={
            'update-stocks-daily': {
                'task': 'app.tasks.stock_tasks.update_all_stocks',
                'schedule': crontab(minute=0, hour='*/6'),  # Every 6 hours
            },
        }
    )
    
    return celery 