from pydantic import BaseModel


class ConditionResponse(BaseModel):
    title: str

    class Config:
        orm_mode = True
