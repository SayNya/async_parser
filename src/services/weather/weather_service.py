from typing import List

from src.orm.models import Weather, WeatherCondition
from src.orm.repositories import weather_repository, day_time_repository, wind_direction_repository, \
    condition_repository, weather_condition_repository
from src.orm.schemas.responses.weather import WeatherResponse
from src.services.base_service import BaseService


class WeatherService(BaseService):

    @staticmethod
    async def save_weather(weather_list: List[dict]):
        for data in weather_list:

            day_time = await day_time_repository.find_by(title=data.pop('day_time'))
            conditions = [await condition_repository.find_by(title=condition) for condition in
                          data.pop('condition')]
            wind_direction = await wind_direction_repository.find_by(direction=data.pop('wind_direction'))

            weather = await weather_repository.create(
                Weather(**data, day_time_id=day_time.id, wind_direction_id=wind_direction.id)
            )

            for condition in conditions:
                await weather_condition_repository.create(WeatherCondition(
                    weather_id=weather.id,
                    condition_id=condition.id
                ))

    # get_weather
    # pydantic
    async def get_weather(self, query):
        #orm = await weather_repository.find_between(**query)
        #model = WeatherResponse.from_orm(orm)
        return None # model
