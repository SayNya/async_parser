from sqlalchemy import Column, Date, Integer, ForeignKey, SmallInteger, String
from sqlalchemy.orm import relationship

from database.orm.models.base import BaseIDModel


class Weather(BaseIDModel):
    __tablename__ = 'weather'
    date = Column(Date)
    t_min = Column(SmallInteger)
    t_max = Column(SmallInteger)
    pressure_min = Column(SmallInteger)
    pressure_max = Column(SmallInteger)
    humidity_min = Column(SmallInteger)
    humidity_max = Column(SmallInteger)
    wind_speed_min = Column(SmallInteger)
    wind_speed_max = Column(SmallInteger)
    url = Column(String(100))

    wind_direction_id = Column(Integer, ForeignKey('wind_directions.id'))
    wind_direction = relationship('WindDirection')

    day_time_id = Column(Integer, ForeignKey('day_times.id'))
    day_time = relationship('DayTime')

    conditions = relationship('WeatherCondition', backref='weather')
