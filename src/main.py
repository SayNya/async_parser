import asyncio

from src.scrapper.weather_scrapper import WeatherScrapper
from src.storage.csv_storage import CSVStorage


async def main():
    weather_scrapper = WeatherScrapper()
    result = await weather_scrapper.scrap_weather()

    writer = CSVStorage()
    await writer.save_content(result)


if __name__ == '__main__':
    asyncio.run(main())
