from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.orm.models.base import BaseIDModel


class Condition(BaseIDModel):
    __tablename__ = 'conditions'
    title = Column(String(100))

    weather = relationship('WeatherCondition', backref='condition')
