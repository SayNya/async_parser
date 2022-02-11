from asyncio import current_task

from prompt_toolkit.eventloop.async_context_manager import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from sqlalchemy.orm import Session, sessionmaker


class AsyncDatabase:
    def __init__(self, db_url: str) -> None:
        self._engine = create_async_engine(db_url, echo=True)
        self._session_factory = async_scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
                class_=AsyncSession
            ),
            scopefunc=current_task
        )

    @asynccontextmanager
    async def session(self):
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
