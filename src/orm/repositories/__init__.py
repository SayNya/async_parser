from src.orm.async_database import async_database
from src.orm.repositories.weather.condition_repository import ConditionRepository
from src.orm.repositories.weather.day_time_repository import DayTimeRepository
from src.orm.repositories.weather.weather_repository import WeatherRepository
from src.orm.repositories.weather.wind_direction_repository import WindDirectionRepository

weather_repository = WeatherRepository(async_database.session)
day_time_repository = DayTimeRepository(async_database.session)
condition_repository = ConditionRepository(async_database.session)
wind_direction_repository = WindDirectionRepository(async_database.session)