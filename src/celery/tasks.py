from datetime import datetime

from asgiref.sync import async_to_sync
from celery import chain
from celery.schedules import crontab

from src.celery.celery import app
from src.utils.date_utlis import get_previous_date
from src.weather_collector.main import save_weather, get_weather


@app.task
def sync_task1():
    return async_to_sync(get_weather)([get_previous_date()])


@app.task
def sync_task2(weather_list):
    for weather in weather_list:
        weather['date'] = datetime.strptime(weather['date'][:10], '%Y-%m-%d').date()

    return async_to_sync(save_weather)(weather_list)


@app.task
def save_previous_weather():
    chain(
        sync_task1.s(),
        sync_task2.s()
    ).apply_async()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=5, hour=0), save_previous_weather.s())
