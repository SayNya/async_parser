from fastapi.responses import StreamingResponse

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

            conditions = [await self.condition_repository.find_by(title=condition) for condition in
                          data.pop('conditions')]
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

        orm_models = await self.weather_repository.find_between(**query.dict()) if query.start_date \
            else await self.weather_repository.find_all()

        pydantic_models = [WeatherResponse.from_orm(model) for model in orm_models]
        return pydantic_models

    async def get_weather_csv(self, query: WeatherParameters) -> StreamingResponse:
        pydantic_models = await self.get_weather_json(query)
        translate_conditions = {
            'малооблачно': 'partly_cloudy',
            'кратковременный дождь': 'short_rain',
            'снег': 'snow',
            'облачно': 'cloudy',
            'пасмурно': 'mainly_cloudy',
            'ясно': 'clear',
            'дождь': 'rain',
        }
        results = []
        for model in pydantic_models:

            full_conditions = {
                'partly_cloudy': False,
                'short_rain': False,
                'snow': False,
                'cloudy': False,
                'mainly_cloudy': False,
                'clear': False,
                'rain': False,
            }
            dict_model = model.dict()

            conditions = dict_model.pop('conditions')

            for condition in conditions:
                full_conditions[translate_conditions[condition]] = True

            dict_model |= full_conditions
            results.append(dict_model)
        response = self.csv_service.get_csv_response(results)
        return response
