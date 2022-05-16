""" Style over metronome """
from model.exercise import Exercise
from music_theory.style import Style
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome

class MetronomeStyle():
    """ Metronome style class
    Example: Play samba over 2-
    PROTOCOL: AbstractPractice
    """
    def __init__(self):
        self._metronome = Metronome()
        self._style = Style()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return self._metronome.category

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns metronome exercises """
        rnd_style = self._style.get_random_style()

        output = self._metronome.get_exercise(quantity, guitar)
        output.title += " Style"
        output.description += f" on {rnd_style}"
        return output
