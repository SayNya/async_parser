import asyncio
from datetime import date
from src.containers.container import Container
from dependency_injector.wiring import Provide, inject
from src.services.weather.weather_service import WeatherService
from src.weather_collector.scrapper.weather_scrapper import WeatherScrapper
from src.utils.date_utlis import get_dates


@inject
async def main(weather_service: WeatherService = Provide[Container.weather_service]):
    date_list = get_dates(start_date=date(2022, 1, 1), end_date=date(2022, 1, 2))
    weather_scrapper = WeatherScrapper()
    weather = await weather_scrapper.scrap_content(date_list)
    await weather_service.save_weather(weather)


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[__name__])
    asyncio.run(main())
