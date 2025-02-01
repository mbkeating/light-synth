from abc import ABC, abstractmethod

class ILocationToNote(ABC):

    @abstractmethod
    def get_notes(self, source_locations):
        pass