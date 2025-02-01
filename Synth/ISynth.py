from abc import ABC, abstractmethod

class ISynth(ABC):
    @abstractmethod
    def play(self, notes):
        pass