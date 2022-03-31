""" Any note can be used with any chord """
from model import exercise, exercise_step
from practice import abstract_practice
from practice.practice_category import PracticeCategory
from music_theory.key_signature import KeySignature

class AnyNoteAnyChord(abstract_practice.AbstractPractice):
    """ Any note any chord class """

    _TITLE = "Any note any chord"
    _SUBTITLE = "Which X chord can contain Y?\r\n(play them too)"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.THEORY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random chord exercises """
        random_steps = []
        key_signature = KeySignature()

        while len(random_steps) < quantity:
            chord_note = key_signature.get_random_note()
            melody_notes = []
            melody_notes_txt = ""
            while len(melody_notes) < 4:
                melody_note = key_signature.get_random_relative_note(chord_note)
                if any([melody_note in melody_notes, melody_note == chord_note]):
                    continue
                melody_notes.append(melody_note)
                if len(melody_notes) > 1:
                    melody_notes_txt += " | "
                melody_notes_txt += melody_note

            random_step = exercise_step.ExerciseStep(
                f"Chord: {chord_note}",
                f"Notes: {melody_notes_txt}")
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output
            