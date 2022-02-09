from sqlalchemy import select


class BaseRepository:
    model = None

    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    async def create(self, model) -> None:
        async with self.session_factory() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model

    async def find_by(self, **parameters: dict):
        async with self.session_factory() as session:
            query = select(self.model).filter_by(**parameters)
            result = await session.execute(query)
            return result.scalars().first()
