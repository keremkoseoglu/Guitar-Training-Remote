from abc import ABC, abstractmethod
from model import workout


class AbstractFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_workout(self) -> workout.WorkOut:
        pass

