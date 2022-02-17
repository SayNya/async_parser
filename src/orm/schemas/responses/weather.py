from datetime import date

from pydantic import BaseModel
from pydantic.class_validators import validator

from src.orm.models import Condition, WindDirection, DayTime


class WeatherResponse(BaseModel):
    date: date
    t_min: int
    t_max: int
    pressure_min: int
    pressure_max: int
    humidity_min: int
    humidity_max: int
    wind_speed_min: int
    wind_speed_max: int
    url: str
    day_time: str
    wind_direction: str
    conditions: list[str]

    @validator('day_time', pre=True)
    def validate_day_time(cls, day_time: DayTime) -> str:
        return day_time.title

    @validator('wind_direction', pre=True)
    def validate_wind_direction(cls, wind_direction: WindDirection) -> str:
        return wind_direction.direction

    @validator('conditions', pre=True)
    def validate_conditions(cls, conditions: list[Condition]) -> list[str]:
        return [condition.title for condition in conditions]

    class Config:
        orm_mode = True
