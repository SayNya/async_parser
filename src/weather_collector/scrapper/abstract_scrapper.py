from abc import ABC, abstractmethod


class AbstractScrapper(ABC):
    @abstractmethod
    def scrap_content(self, *args, **kwargs):
        pass
