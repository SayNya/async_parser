import asyncio
from datetime import date, timedelta
from time import time

from src.crawler.abstract_crawler import AbstractCrawler
from src.http_client.async_client import AsyncClient
from src.parser.weather_parser import WeatherParser
from src.storage.csv_storage import CSVStorage


class WeatherCrawler(AbstractCrawler):
    def __init__(self):
        self.HEAD_URL = 'https://meteo.by/minsk/retro'

        self.weather_parser = WeatherParser()
        self.csv_storage = CSVStorage()

    async def crawl_content(self):
        date_list = list(self.daterange(end_date=date(2003, 2, 1)))
        async with AsyncClient() as async_client:
            tasks = []
            for dte in date_list:
                task = asyncio.create_task(async_client.get_content(self.HEAD_URL + dte))
                tasks.append(task)
            t0 = time()
            html_list = await asyncio.gather(*tasks)
            print(time() - t0)

    def daterange(self, start_date=date(2003, 1, 1), end_date=date.today()):
        for n in range(int((end_date - start_date).days)):
            yield (start_date + timedelta(n)).strftime(f'{self.HEAD_URL}/%Y-%m-%d')
