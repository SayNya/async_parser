from abc import ABC, abstractmethod


class AbstractParser(ABC):
    @abstractmethod
    def parse_content(self, html, *args, **kwargs):
        pass
