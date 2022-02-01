from datetime import date, timedelta

from src.crawler.abstract_crawler import AbstractCrawler
from src.http_client.async_client import AsyncClient
from src.parser.weather_parser import WeatherParser
from src.storage.csv_storage import CSVStorage


class WeatherCrawler(AbstractCrawler):
    def __init__(self):
        self.HEAD_URL = 'https://meteo.by/minsk/retro/'

        self.weather_parser = WeatherParser()
        self.csv_storage = CSVStorage()

    async def crawl_content(self):
        async with AsyncClient() as async_client:
            pass


def daterange(start_date=date(2003, 1, 1), end_date=date.today()):
    for n in range(int((end_date - start_date).days)):
        yield (start_date + timedelta(n)).strftime("%Y-%m-%d")
