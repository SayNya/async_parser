from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.orm.models.base import BaseIDModel


class DayTime(BaseIDModel):
    __tablename__ = 'day_times'
    title = Column(String(100))
    weather = relationship('Weather')
