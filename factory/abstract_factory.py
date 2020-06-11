""" Abstract practice factory """
from abc import ABC, abstractmethod
from model import workout



class AbstractFactory(ABC): # pylint: disable=R0903
    """ Abstract factory for practices """
    @abstractmethod
    def get_workout(self, guitar: dict = None) -> workout.WorkOut:
        """ Returns a new workout """
