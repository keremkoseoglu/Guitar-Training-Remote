from abc import ABC, abstractmethod
from model import exercise
from music_theory import position

class AbstractPractice(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_exercise(self, quantity: int) -> exercise.Exercise:
        pass

    def get_random_position_suggestion_text(self) -> str:
        position_obj = position.Position()
        random_position = str(position_obj.get_random_position())
        return "Suggested position: " + random_position
