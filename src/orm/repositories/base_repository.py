from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.orm.models.base import Base


class BaseRepository:
    model: Base = None

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    async def create(self, model: model) -> model:
        async with self.session_factory() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model

    async def find_by(self, **parameters: dict) -> model:
        async with self.session_factory() as session:
            query = select(self.model).filter_by(**parameters)
            result = await session.execute(query)
            return result.scalars().first()
