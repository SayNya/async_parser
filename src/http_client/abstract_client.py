from abc import ABC, abstractmethod


class AbstractClient(ABC):
    @abstractmethod
    def get_content(self, url):
        pass

    def __aenter__(self):
        pass

    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
