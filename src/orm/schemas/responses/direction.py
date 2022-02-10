from pydantic import BaseModel


class DirectionResponse(BaseModel):
    direction: str

    class Config:
        orm_mode = True
