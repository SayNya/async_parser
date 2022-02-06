from src.orm.async_database import async_database
from src.orm.repositories.weather_repository import WeatherRepository

weather_repository = WeatherRepository(async_database.session)
