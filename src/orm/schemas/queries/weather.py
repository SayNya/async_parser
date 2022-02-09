from pydantic import BaseModel


class WeatherParameters(BaseModel):
    start_date: str
    end_date: str
