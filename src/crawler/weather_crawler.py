from datetime import date, timedelta

from src.crawler.abstract_crawler import AbstractCrawler
from src.http_client.async_client import AsyncClient


class WeatherCrawler(AbstractCrawler):

    async def crawl_content(self):
        dates = self.get_dates(end_date=date(2003, 2, 1))
        urls = self.get_urls(dates)

        async with AsyncClient() as async_client:
            for url in urls:
                try:
                    yield await async_client.get_html(url), url
                except:
                    pass

    @staticmethod
    def get_dates(start_date=date(2003, 1, 1), end_date=date.today()):
        return [(start_date + timedelta(n)).strftime(f'%Y-%m-%d') for n in range(int((end_date - start_date).days))]

    @staticmethod
    def get_urls(dates):
        return [f'https://meteo.by/minsk/retro/{dte}' for dte in dates]
