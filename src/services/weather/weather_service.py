from fastapi.responses import StreamingResponse
from pydantic import parse_obj_as

from src.orm.models import Weather, WeatherCondition
from src.orm.repositories import WeatherRepository, DayTimeRepository, ConditionRepository, WindDirectionRepository, \
    WeatherConditionRepository
from src.orm.schemas.queries.weather import WeatherParameters
from src.orm.schemas.responses.weather import WeatherResponse
from src.services.csv.csv_service import CSVService


class WeatherService:
    def __init__(self,
                 weather_repository: WeatherRepository,
                 day_time_repository: DayTimeRepository,
                 condition_repository: ConditionRepository,
                 wind_direction_repository: WindDirectionRepository,
                 weather_condition_repository: WeatherConditionRepository,
                 csv_service: CSVService,
                 ) -> None:
        self.weather_repository: WeatherRepository = weather_repository
        self.day_time_repository: DayTimeRepository = day_time_repository
        self.condition_repository: ConditionRepository = condition_repository
        self.wind_direction_repository: WindDirectionRepository = wind_direction_repository
        self.weather_condition_repository: WeatherConditionRepository = weather_condition_repository
        self.csv_service: CSVService = csv_service

    async def save_weather(self, weather_list: list[dict]) -> None:
        for data in weather_list:

            day_time = await self.day_time_repository.find_by(title=data.pop('day_time'))
            print(day_time)
            conditions = [await self.condition_repository.find_by(title=condition) for condition in
                          data.pop('condition')]
            wind_direction = await self.wind_direction_repository.find_by(direction=data.pop('wind_direction'))

            weather = await self.weather_repository.create(
                Weather(**data, day_time_id=day_time.id, wind_direction_id=wind_direction.id)
            )

            for condition in conditions:
                await self.weather_condition_repository.create(WeatherCondition(
                    weather_id=weather.id,
                    condition_id=condition.id
                ))

    async def get_weather_json(self, query: WeatherParameters) -> list[WeatherResponse]:
        if query.start_date:
            orm_models = await self.weather_repository.find_between(**query.dict())
        else:
            orm_models = await self.weather_repository.find_all()
        response_list = parse_obj_as(list[WeatherResponse], orm_models)

        return response_list

    async def get_weather_csv(self, query: WeatherParameters) -> StreamingResponse:
        if query.start_date:
            orm_models: list[Weather] = await self.weather_repository.find_between(**query.dict())
        else:
            orm_models: list[Weather] = await self.weather_repository.find_all()

        response_list = parse_obj_as(list[WeatherResponse], orm_models)

        response = self.csv_service.convert_weather_to_csv_response(response_list)
        return response
