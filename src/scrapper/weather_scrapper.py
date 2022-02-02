from src.crawler.weather_crawler import WeatherCrawler
from src.parser.weather_parser import WeatherParser
from src.scrapper.abstract_scrapper import AbstractScrapper


class WeatherScrapper(AbstractScrapper):
    def __init__(self):
        self.crawler = WeatherCrawler()
        self.parser = WeatherParser()

    async def scrap_weather(self):
        result = []

        async for html, url in self.crawler.crawl_content():
            data = await self.parser.parse_content(html, url)
            result.extend(data)

        return result
