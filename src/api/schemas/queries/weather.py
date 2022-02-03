from pydantic import BaseModel


class WeatherParameters(BaseModel):
    path: str
