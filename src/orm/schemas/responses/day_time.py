from pydantic import BaseModel


class DayTimeResponse(BaseModel):
    title: str

    class Config:
        orm_mode = True
