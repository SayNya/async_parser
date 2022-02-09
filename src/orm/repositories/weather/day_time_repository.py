from src.orm.models import DayTime
from src.orm.repositories.base_repository import BaseRepository


class DayTimeRepository(BaseRepository):
    model = DayTime
