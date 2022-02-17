import asyncio

from src.core.settings import settings
from src.orm.async_database import AsyncDatabase
from src.orm.models import *


class Base:
    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory
        self.condition_list = ('малооблачно', 'кратковременный дождь', 'снег', 'облачно', 'пасмурно', 'ясно', 'дождь')
        self.day_time_list = ('ночь', 'день', 'утро', 'вечер')
        self.wind_direction_list = ('ю', 'с', 'з', 'в', 'ю-з', 'ю-в', 'с-з', 'с-в')

    async def create(self) -> None:
        async with self.session_factory() as session:
            condition_models = [Condition(title=title) for title in self.condition_list]
            day_time_models = [DayTime(title=title) for title in self.day_time_list]
            wind_direction_models = [WindDirection(direction=direction) for direction in self.wind_direction_list]
            session.add_all(condition_models)
            session.add_all(day_time_models)
            session.add_all(wind_direction_models)
            await session.commit()


async_database = AsyncDatabase(settings.database_url)
base = Base(async_database.session)

asyncio.run(base.create())
