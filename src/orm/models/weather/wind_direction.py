from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.orm.models.base import BaseIDModel


class WindDirection(BaseIDModel):
    __tablename__ = 'wind_direction'
    direction = Column(String(100), unique=True)
    weather = relationship('Weather', back_populates='wind_direction')
