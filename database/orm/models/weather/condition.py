from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database.orm.models.base import BaseIDModel


class Condition(BaseIDModel):
    __tablename__ = 'conditions'
    name = Column(String(100))

    weather = relationship('WeatherCondition', backref='condition')
