import asyncio
from datetime import date

from dependency_injector.wiring import Provide, inject

from src.containers.container import Container
from src.services.weather.weather_service import WeatherService
from src.weather_collector.scrapper.weather_scrapper import WeatherScrapper


@inject
async def main(dates: list[date], weather_service: WeatherService = Provide[Container.weather_service]):
    weather_scrapper = WeatherScrapper()
    weather = await weather_scrapper.scrap_content(dates)
    await weather_service.save_weather(weather)


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[__name__])
    asyncio.run(main())
