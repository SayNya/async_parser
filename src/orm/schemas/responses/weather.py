from datetime import date

from pydantic import BaseModel

from src.orm.schemas.responses.day_time import DayTimeResponse
from src.orm.schemas.responses.direction import DirectionResponse


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
    day_time: DayTimeResponse
    wind_direction: DirectionResponse

    class Config:
        orm_mode = True
