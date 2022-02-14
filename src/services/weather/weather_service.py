from fastapi.responses import StreamingResponse

from src.orm.models import Weather, WeatherCondition
from src.orm.repositories import WeatherRepository, DayTimeRepository, ConditionRepository, WindDirectionRepository, \
    WeatherConditionRepository
from src.orm.schemas.queries.weather import WeatherParameters
from src.orm.schemas.responses.weather import WeatherResponse
from src.services.csv.csv_service import CSVService
from src.utils.string_utils import weather_model_to_csv_line


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

        response = [WeatherResponse(
            date=model.date,
            t_min=model.t_min,
            t_max=model.t_max,
            pressure_min=model.pressure_min,
            pressure_max=model.pressure_max,
            humidity_min=model.humidity_min,
            humidity_max=model.humidity_max,
            wind_speed_min=model.wind_speed_min,
            wind_speed_max=model.wind_speed_max,
            url=model.url,
            day_time=model.day_time.title,
            wind_direction=model.wind_direction.direction,
            conditions=[x.title for x in model.conditions]
        ) for model in orm_models]

        return response

    async def get_weather_csv(self, query: WeatherParameters) -> StreamingResponse:
        response_list = await self.get_weather_json(query)

        response = self.csv_service.get_csv_response(response_list)
        return response
