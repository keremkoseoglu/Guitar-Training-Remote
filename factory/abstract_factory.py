""" Abstract practice factory """
from typing import Protocol, List
from model import workout


class AbstractFactory(Protocol):  # pylint: disable=R0903
    """ Abstract factory for practices """

    def get_workout(self, guitar: dict = None, exclude_classes: List[str] = None) -> workout.WorkOut:
        """ Returns a new workout """
