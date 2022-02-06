import contextlib
from asyncio import current_task
from contextlib import AbstractContextManager
from typing import Callable

from prompt_toolkit.eventloop.async_context_manager import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from sqlalchemy.orm import Session, sessionmaker

from src.core.settings import settings
from src.orm.models.base import Base


class AsyncDatabase:
    def __init__(self, db_uri: str) -> None:
        self._engine = create_async_engine(db_uri, echo=True)
        self._session_factory = async_scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
                class_=AsyncSession
            ),
            scopefunc=current_task
        )

    async def truncate_database(self) -> None:
        async with contextlib.closing(self._engine.connect()) as con:
            trans = await con.begin()
            for table in reversed(Base.sorted_tables):
                await con.execute(table.delete())
            await trans.commit()

    async def drop_database(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async def create_database(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    async def session(self) -> Callable[..., AbstractContextManager[AsyncSession]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async_database = AsyncDatabase(settings.database_uri)
