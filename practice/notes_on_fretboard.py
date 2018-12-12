from model import exercise, exercise_step
from music_theory import note
from practice import abstract_practice
import random


class NotesOnFretboard(abstract_practice.AbstractPractice):

    _MAX_NOTE_PER_STEP = 3
    _TITLE = "Fretboard single note memorization"
    _SUBTITLE = "Find the given note(s) on each string"

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        note_obj = note.Note()
        random_steps = []

        for step_index in range(0, quantity):
            step_text = ""

            note_count_of_step = random.randint(1, self._MAX_NOTE_PER_STEP)
            notes_of_step = note_obj.get_random_notes(note_count_of_step)
            for note_of_step in notes_of_step:
                if step_text != "":
                    step_text += ", "
                step_text += note_of_step

            random_step = exercise_step.ExerciseStep(step_text)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
