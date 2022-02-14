import asyncio
from datetime import date

from src.weather_collector.scrapper.weather_scrapper import WeatherScrapper
from src.weather_collector.utils.date_utlis import get_dates


async def main():
    date_list = get_dates(start_date=date(2022, 1, 1), end_date=date(2022, 1, 15))
    weather_scrapper = WeatherScrapper()
    weather = await weather_scrapper.scrap_content(date_list)


if __name__ == '__main__':
    asyncio.run(main())
