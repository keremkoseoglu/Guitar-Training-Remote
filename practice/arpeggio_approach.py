""" Arpeggio with chord tone approach """
from enum import Enum
from random import randint
from model import exercise
from practice.abstract_practice import AbstractPractice
from practice.arpeggio import Arpeggio
from practice.practice_category import PracticeCategory

class ApproachDirection(Enum):
    """ Approach direction """
    BELOW = 1
    ABOVE = 2
    MIXED = 3

class ArpeggioChordToneApproach(AbstractPractice):
    """ Arpeggio with chord tone approach """
    _TITLE = "Approach arpeggio"

    def __init__(self):
        self._arpeggio = Arpeggio()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return self._arpeggio.category

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns arpeggio exercise """
        output = self._arpeggio.get_exercise(quantity, guitar)
        if output is None:
            return output

        output.title = ArpeggioChordToneApproach._TITLE
        dir_index = randint(0, len(ApproachDirection) - 1)
        output.title += f" from {ApproachDirection(dir_index).name}"

        return output
