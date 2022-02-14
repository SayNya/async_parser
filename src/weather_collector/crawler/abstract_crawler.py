from abc import ABC, abstractmethod


class AbstractCrawler(ABC):
    @abstractmethod
    def crawl_content(self, *args, **kwargs):
        pass
