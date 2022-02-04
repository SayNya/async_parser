from sqlalchemy import Column
from sqlalchemy.orm import relationship

from database.orm.models.base import BaseIDModel


class WindDirection(BaseIDModel):
    __tablename__ = 'wind_directions'
    direction = Column()
    weather = relationship('Weather')
