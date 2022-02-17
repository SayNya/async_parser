from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.orm.models.weather import Weather
from src.orm.repositories.base_repository import BaseRepository


class WeatherRepository(BaseRepository):
    model: Weather = Weather

    async def find_between(self, start_date: date, end_date: date) -> list[Weather]:
        async with self.session_factory() as session:
            query = select(Weather). \
                options(
                selectinload(Weather.day_time),
                selectinload(Weather.wind_direction),
                selectinload(Weather.conditions),
            ). \
                filter(self.model.date >= start_date, self.model.date <= end_date)

            result = await session.execute(query)

            return result.scalars().all()

    async def find_all(self) -> list[Weather]:
        async with self.session_factory() as session:
            query = select(Weather). \
                options(
                selectinload(Weather.day_time),
                selectinload(Weather.wind_direction),
                selectinload(Weather.conditions),
            )
            result = await session.execute(query)

            return result.scalars().all()
