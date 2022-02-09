from src.orm.models import Condition
from src.orm.repositories.base_repository import BaseRepository


class ConditionRepository(BaseRepository):
    model = Condition
