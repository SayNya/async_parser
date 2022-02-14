from datetime import date

from src.weather_collector.crawler.weather_crawler import WeatherCrawler
from src.weather_collector.parser.weather_parser import WeatherParser
from src.weather_collector.scrapper.abstract_scrapper import AbstractScrapper


class WeatherScrapper(AbstractScrapper):
    def __init__(self):
        self.crawler = WeatherCrawler()
        self.parser = WeatherParser()

    async def scrap_content(self, date_list: list[date]) -> list[dict]:
        result = []
        async for html, url, current_date in self.crawler.crawl_content(date_list):
            data = await self.parser.parse_content(html, url, current_date)
            result.extend(data)

        return result
