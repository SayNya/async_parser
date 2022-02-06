from sqlalchemy import Column, Date, Integer, ForeignKey, SmallInteger, String
from sqlalchemy.orm import relationship

from src.orm.models.base import BaseIDModel


class Weather(BaseIDModel):
    __tablename__ = 'weather'
    date = Column(Date)
    t_min = Column(Integer)
    t_max = Column(Integer)
    pressure_min = Column(Integer)
    pressure_max = Column(Integer)
    humidity_min = Column(Integer)
    humidity_max = Column(Integer)
    wind_speed_min = Column(Integer)
    wind_speed_max = Column(Integer)
    url = Column(String(100))

    wind_direction_id = Column(Integer, ForeignKey('wind_directions.id'))
    wind_direction = relationship('WindDirection', back_populates='weather')

    day_time_id = Column(Integer, ForeignKey('day_times.id'))
    day_time = relationship('DayTime')

    conditions = relationship('WeatherCondition', backref='weather')
