import io
from typing import List

from pydantic import parse_obj_as

from src.orm.models import Weather, WeatherCondition
from src.orm.repositories import weather_repository, day_time_repository, wind_direction_repository, \
    condition_repository, weather_condition_repository
from src.orm.schemas.queries.weather import WeatherParameters
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

    @staticmethod
    async def get_weather_json(query: WeatherParameters):
        if query.dict()['start_date']:
            orm_models = await weather_repository.find_between(**query.dict())
        else:
            orm_models = await weather_repository.find_all()
        response_list = parse_obj_as(list[WeatherResponse], orm_models)

        return response_list

    @staticmethod
    async def get_weather_csv(query: WeatherParameters):
        if query.dict()['start_date']:
            orm_models: list[Weather] = await weather_repository.find_between(**query.dict())
        else:
            orm_models: list[Weather] = await weather_repository.find_all()

        response_list = parse_obj_as(list[WeatherResponse], orm_models)

        stream = io.StringIO()

        stream.write('date;day_time;t_min;t_max;pressure_min;pressure_max;humidity_min;'
                     'humidity_max;wind_speed_min;wind_speed_max;wind_direction;url\n')

        for model in response_list:
            line = model_to_csv_line(model)
            print(line)
            stream.write(line)

        return stream


def model_to_csv_line(model: WeatherResponse):
    return f'{model.date};{model.day_time.title};{model.t_min};{model.t_max};{model.pressure_min};' \
           f'{model.pressure_max};{model.humidity_min};{model.humidity_max};{model.wind_speed_min};' \
           f'{model.wind_speed_max};{model.wind_direction.direction};{model.url}\n'
