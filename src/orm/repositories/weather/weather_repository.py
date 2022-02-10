from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.orm.models import WindDirection, DayTime
from src.orm.models.weather import Weather
from src.orm.repositories.base_repository import BaseRepository


class WeatherRepository(BaseRepository):
    model = Weather

    async def find_between(self, **kwargs):
        async with self.session_factory() as session:
            query = select(Weather). \
                options(
                selectinload(Weather.day_time),
                selectinload(Weather.wind_direction),
            ). \
                join(DayTime). \
                join(WindDirection). \
                filter(self.model.date >= kwargs['start_date'], self.model.date <= kwargs['end_date'])

            result = await session.execute(query)
            result = result.scalars().all()

            return result

    async def find_all(self):
        async with self.session_factory() as session:
            query = select(Weather). \
                options(
                selectinload(Weather.day_time),
                selectinload(Weather.wind_direction),
            ). \
                join(DayTime). \
                join(WindDirection)

            result = await session.execute(query)
            result = result.scalars().all()

            return result
