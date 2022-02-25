from src.containers.container import Container
from src.weather_collector.scrapper.weather_scrapper import WeatherScrapper


async def get_weather(dates):
    weather_scrapper = WeatherScrapper()
    return await weather_scrapper.scrap_content(dates)


async def save_weather(weather):
    container = Container()
    weather_service = container.weather_service()
    await weather_service.save_weather(weather)
