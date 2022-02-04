import asyncio

from src.weather_collector.scrapper.weather_scrapper import WeatherScrapper
from src.weather_collector.storage.csv_storage import CSVStorage


async def main():
    weather_scrapper = WeatherScrapper()
    result = await weather_scrapper.scrap_weather()

    writer = CSVStorage()
    return await writer.save_content(result)


def get_csv_data():
    path = asyncio.run(main())
    return path

get_csv_data()