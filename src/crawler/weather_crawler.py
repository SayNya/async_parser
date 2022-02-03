import os
from datetime import date, timedelta

from dotenv import load_dotenv, find_dotenv

from src.crawler.abstract_crawler import AbstractCrawler
from src.http_client.async_client import AsyncClient

load_dotenv(find_dotenv())


class WeatherCrawler(AbstractCrawler):
    def __init__(self):
        self.HEAD_URL = os.environ.get('HEAD_URL')

    async def crawl_content(self):

        dates = self.get_dates()
        async with AsyncClient() as async_client:
            for dte in dates:
                url = f'{self.HEAD_URL}' + dte
                yield await async_client.get_html(url), url, dte

    @staticmethod
    def get_dates(start_date=date(2003, 1, 1), end_date=date.today()):
        for n in range(int((end_date - start_date).days)):
            yield (start_date + timedelta(n)).strftime(f'%Y-%m-%d')
