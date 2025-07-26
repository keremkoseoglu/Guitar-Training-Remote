""" XLET exercises over metronome """
import random
from model.exercise import Exercise
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome

class MetronomeXlet():
    """ Metronome XLET class
    Example: 3let over 72 BPM 2-
    PROTOCOL: AbstractPractice
    """
    _LETS = [2, 3, 4, 5, 6]

    def __init__(self):
        self._metronome = Metronome()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return self._metronome.category

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns metronome exercises """
        xlet_index = random.randint(0, len(MetronomeXlet._LETS) - 1)
        xlet = MetronomeXlet._LETS[xlet_index]

        output = self._metronome.get_exercise(quantity, guitar)
        output.title += " XLET"
        output.description += f" in {str(xlet)}lets"
        return output
