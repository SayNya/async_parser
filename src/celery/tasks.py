import asyncio

from src.celery.celery import app
from src.containers.container import Container
from src.utils.date_utlis import get_previous_date
from src.weather_collector.main import main
from celery.schedules import crontab


@app.task
def save_previous_weather():
    container = Container()
    container.wire(modules=[__name__])
    dates = [get_previous_date()]
    asyncio.run(main(dates))


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=5, hour=0), save_previous_weather.s())
