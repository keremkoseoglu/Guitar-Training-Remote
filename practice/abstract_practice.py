from abc import ABC, abstractmethod
from model import exercise
from model.guitar import Guitar
from music_theory.position import Position


class AbstractPractice(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:
        pass

    def get_random_position_suggestion_text(self) -> str:
        random_position = str(Position.get_random_position())
        return "Suggested position: " + random_position
