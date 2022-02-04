from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database.orm.models.base import BaseIDModel


class DayTime(BaseIDModel):
    __tablename__ = 'day_times'
    name = Column(String(100))
    weather = relationship('Weather')
