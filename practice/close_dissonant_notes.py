""" Close dissonant notes """
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.common_chord_notes import CommonChordNotes
from model.exercise import Exercise

class CloseDissonantNotes(AbstractPractice):
    """ Close dissonant notes """
    _TITLE = "Close dissonant notes"
    _SUBTITLE = "Play among chords"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns random chord exercises """
        result = CommonChordNotes().get_exercise(quantity, guitar)
        result.title = CloseDissonantNotes._TITLE
        result.description = CloseDissonantNotes._SUBTITLE
        return result
