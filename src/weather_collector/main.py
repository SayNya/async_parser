import asyncio

from src.services.weather.weather_service import WeatherService
from src.weather_collector.scrapper.weather_scrapper import WeatherScrapper
from src.weather_collector.storage.csv_storage import CSVStorage


async def main():
    weather_scrapper = WeatherScrapper()
    weather = await weather_scrapper.scrap_weather()

    service = WeatherService()
    await service.save_weather(weather)

    # writer = CSVStorage()
    # await writer.save_content(result)


if __name__ == '__main__':
    asyncio.run(main())
