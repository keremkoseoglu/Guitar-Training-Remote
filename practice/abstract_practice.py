""" Abstract practice module """
from abc import ABC, abstractmethod
from model import exercise
from music_theory.position import Position


class AbstractPractice(ABC):
    """ Abstract practice class
    All other practices should be inherited from this class
    """

    @abstractmethod
    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns the exercise object """

    @staticmethod
    def get_random_position_suggestion_text() -> str:
        """ Random suggestion position text """
        random_position = str(Position.get_random_position())
        return "Suggested position: " + random_position
