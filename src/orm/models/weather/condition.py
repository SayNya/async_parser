from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.orm.models.base import BaseIDModel


class Condition(BaseIDModel):
    __tablename__ = 'condition'
    title = Column(String(100), unique=True)

    weather = relationship('Weather', back_populates='conditions', secondary='weather_condition')
