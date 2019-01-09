from abc import ABC, abstractmethod


class DefaultBox(ABC):
    @abstractmethod
    def add_to_layout(self):
        pass

    @abstractmethod
    def translate(self):
        pass
