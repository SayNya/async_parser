from src.orm.models import WeatherCondition
from src.orm.repositories.base_repository import BaseRepository


class WeatherConditionRepository(BaseRepository):
    model: WeatherCondition = WeatherCondition
