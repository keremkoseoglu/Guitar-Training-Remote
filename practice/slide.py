""" Guitar slide module """
from model import exercise
from practice import abstract_practice
from practice.notes_on_fretboard import NotesOnFretboard


class Slide(abstract_practice.AbstractPractice):
    """ Guitar slide exercise """

    _TITLE = "Slide guitar"
    _SUBTITLE = "Play the note(s) on each string with slide"

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns exercise """
        string_count = guitar["strings"]
        if string_count < 6:
            return None

        output = NotesOnFretboard().get_exercise(quantity, guitar)
        output.title = Slide._TITLE
        output.description = Slide._SUBTITLE
        return output
