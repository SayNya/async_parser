from celery import Celery

from src.core.settings import settings

app = Celery(
    __name__,
    broker=settings.celery_broker_url,
    include=['src.celery.tasks']
)

app.conf.timezone = 'Europe/Minsk'
