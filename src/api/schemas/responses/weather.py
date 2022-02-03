from pydantic import BaseModel


class WeatherResponse(BaseModel):
    date: str
    day_time: str
    t_min: int
    t_max: int
    state: str
    pressure_min: int
    pressure_max: int
    humidity_min: int
    humidity_max: int
    wind_speed_min: int
    wind_speed_max: int
    wind_direction: str
    url: str
