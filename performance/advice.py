""" Advice module """
from copy import copy
from random import randint
from config import get_configuration

class Advice:
    """ Performance advice class """
    def __new__(cls):
        if not hasattr(cls, "_SINGLETON"):
            cls._SINGLETON = super(Advice, cls).__new__(cls)
        return cls._SINGLETON

    def __init__(self):
        self._advices_read = False
        self._advices = []

    def get_random_advice(self) -> str:
        """ Returns a random advice """
        self._lazy_read_advices()
        if len(self._advices) == 0:
            return ""
        random_index = randint(0, len(self._advices) - 1)
        return self._advices[random_index]

    def _lazy_read_advices(self):
        """ Lazy read advices """
        if self._advices_read:
            return
        config = get_configuration()
        self._advices = copy(config["advices"])
        self._advices_read = True
        