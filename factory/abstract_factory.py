""" Abstract practice factory """
from typing import Protocol
from model import workout



class AbstractFactory(Protocol): # pylint: disable=R0903
    """ Abstract factory for practices """
    def get_workout(self, guitar: dict = None) -> workout.WorkOut:
        """ Returns a new workout """
        ...
