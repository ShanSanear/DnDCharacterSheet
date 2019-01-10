from abc import ABC, abstractmethod


class DefaultBox(ABC):
    @abstractmethod
    def add_to_layout(self, **kwargs):
        pass

    @abstractmethod
    def translate(self, **kwargs):
        pass
