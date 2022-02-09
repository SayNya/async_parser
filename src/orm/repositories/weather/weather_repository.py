from src.orm.models.weather import Weather
from src.orm.repositories.base_repository import BaseRepository


class WeatherRepository(BaseRepository):
    model = Weather
