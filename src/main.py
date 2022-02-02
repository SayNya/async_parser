import asyncio

from src.scrapper.weather_scrapper import WeatherScrapper
from src.storage.csv_storage import CSVStorage

if __name__ == '__main__':
    weather_crawler = WeatherScrapper()
    result = asyncio.get_event_loop().run_until_complete(weather_crawler.scrap_weather())

    writer = CSVStorage()
    asyncio.get_event_loop().run_until_complete(writer.save_content(result))
