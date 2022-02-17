from src.orm.models import WindDirection
from src.orm.repositories.base_repository import BaseRepository


class WindDirectionRepository(BaseRepository):
    model: WindDirection = WindDirection
