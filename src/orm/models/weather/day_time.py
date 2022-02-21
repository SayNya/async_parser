from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.orm.models.base import BaseIDModel


class DayTime(BaseIDModel):
    __tablename__ = 'day_time'
    title = Column(String(100), unique=True)
    weather = relationship('Weather', back_populates='day_time')
