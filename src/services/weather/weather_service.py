from typing import List

from src.orm.models import Weather
from src.orm.repositories import weather_repository, day_time_repository, wind_direction_repository, \
    condition_repository
from src.services.base_service import BaseService


class WeatherService(BaseService):

    async def save_data(self, weather_list: List[dict]):
        data = []
        for weather in weather_list:
            day_time = await day_time_repository.find_by(title=weather.pop('day_time'))
            conditions = [await condition_repository.find_by(title=condition) for condition in weather.pop('condition')]
            wind_direction = await wind_direction_repository.find_by(direction=weather.pop('wind_direction'))
            # data.append(Weather(**weather, day_time=day_time, wind_direction=wind_direction, conditions=conditions))
            data.append(Weather(**weather))
        await weather_repository.bulk_create(data)

    # get_weather
    # pydantic
