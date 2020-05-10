""" Module for notes on strings practice """
from model import exercise, exercise_step
from model.guitar import Guitar
from music_theory import note
from practice import abstract_practice


class NotesOnStrings(abstract_practice.AbstractPractice):
    """ Notes on strings practice class """

    _BASS_STRINGS = 4
    _GUITAR_STRINGS = 6
    _KEYBOARD_OCTAVES = 4
    _TITLE = "Note memorization"

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:
        if guitar == Guitar.KEYS:
            subtitle = "Find the given notes on subsequent octaves"
            strings = NotesOnStrings._KEYBOARD_OCTAVES
        elif guitar == Guitar.BASS:
            subtitle = "Find the given notes on subsequent strings"
            strings = NotesOnStrings._BASS_STRINGS
        else:
            subtitle = "Find the given notes on subsequent strings"
            strings = NotesOnStrings._GUITAR_STRINGS

        note_obj = note.Note()
        random_steps = []

        for step_index in range(0, quantity): # pylint: disable=W0612
            step_text = ""

            notes_of_step = note_obj.get_random_notes(strings)
            for note_of_step in notes_of_step:
                if step_text != "":
                    step_text += ", "
                step_text += note_of_step

            random_step = exercise_step.ExerciseStep(step_text)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, subtitle, random_steps)
        return output
