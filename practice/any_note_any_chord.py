""" Any note can be used with any chord """
from model import exercise, exercise_step
from practice import abstract_practice
from music_theory.note import Note

class AnyNoteAnyChord(abstract_practice.AbstractPractice):
    """ Any note any chord class """

    _TITLE = "Any note any chord"
    _SUBTITLE = "Which X chord can contain Y?"

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random chord exercises """
        random_steps = []
        note = Note()

        while len(random_steps) < quantity:
            chord_note = note.get_random_note()
            melody_notes = []
            melody_notes_txt = ""
            while len(melody_notes) < 4:
                melody_note = note.get_random_note()
                if any([melody_note in melody_notes, melody_note == chord_note]):
                    continue
                melody_notes.append(melody_note)
                if len(melody_notes) > 1:
                    melody_notes_txt += " | "
                melody_notes_txt += melody_note

            random_step = exercise_step.ExerciseStep(
                "Chord: " + chord_note,
                "Notes: " + melody_notes_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
            