from datetime import date

from src.core.settings import settings
from src.weather_collector.crawler.abstract_crawler import AbstractCrawler
from src.weather_collector.http_client.async_client import AsyncClient


class WeatherCrawler(AbstractCrawler):
    def __init__(self):
        self.HEAD_URL = settings.head_url

    async def crawl_content(self, data_list: list[date]) -> (bytes, str, date):
        async with AsyncClient() as async_client:
            for current_date in data_list:
                url = f'{self.HEAD_URL}' + current_date.strftime(f'%Y-%m-%d')

                yield await async_client.get(url), url, date
