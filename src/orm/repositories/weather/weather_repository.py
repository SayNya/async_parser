from sqlalchemy import select

from src.orm.models.weather import Weather
from src.orm.repositories.base_repository import BaseRepository


class WeatherRepository(BaseRepository):
    model = Weather

    async def find_between(self, st):
        async with self.session_factory() as session:
            print(session.query(self.model).filter(start_date <= self.model.date <= end_date))
