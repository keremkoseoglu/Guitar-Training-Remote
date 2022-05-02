""" Module for notes on strings practice """
from model import exercise, exercise_step
from music_theory import note
from practice.practice_category import PracticeCategory


class NotesOnStrings():
    """ Notes on strings practice class
    PROTOCOL: AbstractPractice
    """
    _TITLE = "Note memorization"

    def __init__(self):
        self.min_note_count = None

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns exercise """
        if guitar["kind"] != "instrument":
            return None
        if guitar["strings"] <= 0:
            subtitle = "Find the given notes on subsequent octaves"
            strings = guitar["octaves"]
        else:
            subtitle = "Find the given notes on subsequent strings"
            strings = guitar["strings"]

        note_obj = note.Note()
        random_steps = []

        for step_index in range(0, quantity): # pylint: disable=W0612
            step_text = ""

            note_count = strings
            if self.min_note_count is not None and self.min_note_count > strings:
                note_count = self.min_note_count
            notes_of_step = note_obj.get_random_notes(note_count)
            for note_of_step in notes_of_step:
                if step_text != "":
                    step_text += ", "
                step_text += note_of_step

            random_step = exercise_step.ExerciseStep(step_text)
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            subtitle,
            random_steps,
            practice_category=self.category)

        return output
