from pydantic import BaseModel
from datetime import date

from pydantic.class_validators import validator


class WeatherParameters(BaseModel):
    start_date: date = None
    end_date: date = None

    @validator('end_date')
    def end_start_date_not_empty(cls, v, values):
        if bool(v) ^ bool(values['start_date']):
            raise ValueError('start_date and end_date must be filled or empty')
        return v

    @validator('end_date')
    def end_after_start(cls, v, values):
        if v < values['start_date']:
            raise ValueError('end_date should be before or equal start_day')
        return v