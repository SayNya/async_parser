from datetime import date

from pydantic import BaseModel


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

    class Config:
        orm_mode = True
