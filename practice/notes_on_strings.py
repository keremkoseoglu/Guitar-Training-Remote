from model import exercise, exercise_step
from model.guitar import Guitar
from music_theory import note
from practice import abstract_practice


class NotesOnStrings(abstract_practice.AbstractPractice):

    _STRINGS = 4
    _TITLE = "Note memorization"

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:
        if guitar == Guitar.KEYS:
            subtitle = "Find the given notes on subsequent octaves"
        else:
            subtitle = "Find the given notes on subsequent strings"

        note_obj = note.Note()
        random_steps = []

        for step_index in range(0, quantity):
            step_text = ""

            notes_of_step = note_obj.get_random_notes(self._STRINGS)
            for note_of_step in notes_of_step:
                if step_text != "":
                    step_text += ", "
                step_text += note_of_step

            random_step = exercise_step.ExerciseStep(step_text)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, subtitle, random_steps)
        return output
