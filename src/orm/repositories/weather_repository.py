from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.orm.models.weather.weather import Weather
from src.orm.schemas.responses.weather import WeatherResponse


class WeatherRepository:
    model = Weather

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    async def find_by(self, **parameters: dict) -> Weather:
        async with self.session_factory() as session:
            query = select(Weather).filter_by(**parameters)
            result = await session.execute(query)
            return result.scalars().first()

    async def create(self, model: WeatherResponse) -> None:
        async with self.session_factory() as session:
            session.add(model)
            await session.commit()
