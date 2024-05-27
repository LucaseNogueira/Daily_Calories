from abc import ABC, abstractmethod

class RequestInterface(ABC):

    @abstractmethod
    def to_domain(self):
        pass