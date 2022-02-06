from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.orm.models.base import BaseIDModel


class WindDirection(BaseIDModel):
    __tablename__ = 'wind_directions'
    direction = Column(String(100))
    weather = relationship('Weather', back_populates='wind_direction')
