import asyncio
from datetime import date

from src.weather_collector.scrapper.weather_scrapper import WeatherScrapper
from src.weather_collector.utils.date_utlis import get_dates


async def main(data_list: list | date):
    weather_scrapper = WeatherScrapper()
    weather = await weather_scrapper.scrap_weather(data_list)


if __name__ == '__main__':
    date_list = get_dates(start_date=date(2022, 1, 1), end_date=date(2022, 1, 15))
    asyncio.run(main(date_list))
