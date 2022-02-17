from abc import ABC, abstractmethod


class AbstractClient(ABC):
    @abstractmethod
    async def get(self, url: str) -> bytes:
        pass

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print(exc_val)
            raise exc_type
