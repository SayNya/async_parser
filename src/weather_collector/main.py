import asyncio

from src.weather_collector.scrapper.weather_scrapper import WeatherScrapper
from src.weather_collector.storage.csv_storage import CSVStorage


async def main():
    weather_scrapper = WeatherScrapper()
    result = await weather_scrapper.scrap_weather()

    #  service

    writer = CSVStorage()
    await writer.save_content(result)


if __name__ == '__main__':
    asyncio.run(main())
