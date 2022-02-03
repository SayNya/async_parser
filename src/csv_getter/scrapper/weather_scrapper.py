from src.csv_getter.crawler.weather_crawler import WeatherCrawler
from src.csv_getter.parser.weather_parser import WeatherParser
from src.csv_getter.scrapper.abstract_scrapper import AbstractScrapper


class WeatherScrapper(AbstractScrapper):
    def __init__(self):
        self.crawler = WeatherCrawler()
        self.parser = WeatherParser()

    async def scrap_weather(self):
        result = []
        async for html, url, dte in self.crawler.crawl_content():
            data = await self.parser.parse_content(html, url, dte)
            result.extend(data)

        return result
