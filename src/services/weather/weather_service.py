from fastapi.responses import StreamingResponse

from src.enums.conditions import Conditions
from src.orm.models import Weather, WeatherCondition
from src.orm.repositories import WeatherRepository, DayTimeRepository, ConditionRepository, WindDirectionRepository, \
    WeatherConditionRepository
from src.orm.schemas.queries.weather import WeatherParameters
from src.orm.schemas.responses.weather import WeatherResponse
from src.services.csv.csv_service import CSVService

CONDITIONS_MAPPING = {
    Conditions.PARTLY_CLOUDY.value: 'partly_cloudy',
    Conditions.SHORT_RAIN.value: 'short_rain',
    Conditions.SNOW.value: 'snow',
    Conditions.CLOUDY.value: 'cloudy',
    Conditions.MAINLY_CLOUDY.value: 'mainly_cloudy',
    Conditions.CLEAR.value: 'clear',
    Conditions.RAIN.value: 'rain'
}


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

    async def get_weather_models(self, query: WeatherParameters) -> list[Weather]:

        return await self.weather_repository.find_between(**query.dict()) if query.start_date \
            else await self.weather_repository.find_all()

    async def get_weather_csv(self, query: WeatherParameters) -> StreamingResponse:
        orm_models = await self.get_weather_models(query)
        pydantic_models = [WeatherResponse.from_orm(model) for model in orm_models]
        dict_model_list = self.__weather_to_csv_dict(pydantic_models)

        response = self.csv_service.get_csv_response(dict_model_list)
        return response

    def __weather_to_csv_dict(self, pydantic_models: list[WeatherResponse]) -> list[dict]:
        dict_model_list = []
        for model in pydantic_models:
            dict_model = model.dict()

            conditions = dict_model.pop('conditions')

            full_conditions = self.__destructure_conditions(conditions)

            dict_model |= full_conditions
            dict_model_list.append(dict_model)
        return dict_model_list

    @staticmethod
    def __destructure_conditions(conditions: list[str]) -> dict:
        full_conditions = {
            'partly_cloudy': False,
            'short_rain': False,
            'snow': False,
            'cloudy': False,
            'mainly_cloudy': False,
            'clear': False,
            'rain': False,
        }

        for condition in conditions:
            full_conditions[CONDITIONS_MAPPING[condition]] = True

        return full_conditions
