from database.orm.async_database import async_database
from database.orm.repositories.weather_repository import WeatherRepository

forecast_repository = WeatherRepository(async_database.session)
