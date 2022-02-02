import aiohttp

from src.http_client.abstract_client import AbstractClient


class AsyncClient(AbstractClient):
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def get_html(self, url):
        async with self.session.get(url) as response:
            return await response.read()
