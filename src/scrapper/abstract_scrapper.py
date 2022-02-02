from abc import ABC, abstractmethod


class AbstractScrapper(ABC):
    @abstractmethod
    def scrap_weather(self):
        pass
