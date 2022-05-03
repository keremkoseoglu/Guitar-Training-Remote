""" Guitar slide module """
from model import exercise
from practice.abstract_practice import AbstractPractice
from practice.notes_on_fretboard import NotesOnFretboard
from practice.practice_category import PracticeCategory


class Slide(AbstractPractice):
    """ Guitar slide exercise """
    _TITLE = "Slide guitar"
    _SUBTITLE = "Play the note(s) on each string with slide"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.LEFT_HAND

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns exercise """
        string_count = guitar["strings"]
        if string_count < 6:
            return None

        output = NotesOnFretboard().get_exercise(quantity, guitar)
        output.title = Slide._TITLE
        output.description = Slide._SUBTITLE
        return output
