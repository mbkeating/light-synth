from abc import ABC, abstractmethod
from typing import List, Tuple
import numpy as np

class ILightLocator(ABC):

    @abstractmethod
    def locate_sources(self, frame: np.ndarray) -> List[Tuple[int, int]]:
        pass