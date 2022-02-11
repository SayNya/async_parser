from abc import ABC, abstractmethod


class AbstractCrawler(ABC):
    @abstractmethod
    def crawl_content(self, data_list: list):
        pass
