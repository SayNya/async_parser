from sqlalchemy import Column, String, Integer, ForeignKey

from src.orm.models.base import BaseIDModel


class WeatherCondition(BaseIDModel):
    __tablename__ = 'weather_condition'
    weather_id = Column(Integer(), ForeignKey('weather.id'), primary_key=True)
    condition_id = Column(Integer(), ForeignKey('condition.id'), primary_key=True)