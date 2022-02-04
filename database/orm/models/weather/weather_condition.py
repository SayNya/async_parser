from sqlalchemy import Column, String, Integer, ForeignKey

from database.orm.models.base import BaseIDModel


class WeatherCondition(BaseIDModel):
    __tablename__ = 'weather_condition'
    name = Column(String(100))
    weather_id = Column(Integer(), ForeignKey('weather.id'))
    condition_id = Column(Integer(), ForeignKey('conditions.id'))
