from sqlalchemy import select


class BaseRepository:
    model = None

    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    async def bulk_create(self, data_list):
        async with self.session_factory() as session:
            session.add_all(data_list)
            await session.commit()

    async def create(self, model) -> None:
        async with self.session_factory() as session:
            session.add_all(model)
            await session.commit()

    async def find_by(self, **parameters: dict):
        async with self.session_factory() as session:
            query = select(self.model).filter_by(**parameters)
            result = await session.execute(query)
            return result.scalars().first()
