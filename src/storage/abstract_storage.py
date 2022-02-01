from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def save_content(self, content):
        pass
