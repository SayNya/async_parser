import aiohttp

from src.decorators.time_decorator import timeit
from src.weather_collector.http_client.abstract_client import AbstractClient


class AsyncClient(AbstractClient):
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await super().__aexit__(exc_type, exc_val, exc_tb)
        await self.session.close()

    @timeit
    async def get(self, url: str) -> bytes:
        async with self.session.get(url) as response:
            return await response.read()
