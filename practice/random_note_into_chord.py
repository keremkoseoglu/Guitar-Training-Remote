""" Random note into chord transition """
from model.exercise import Exercise
from model.exercise_step import ExerciseStep
from music_theory.chord import Chord
from music_theory.key_signature import KeySignature
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory

class RandomNoteIntoChord(AbstractPractice):
    """ Random note into chord transition """
    _TITLE = "Note into chord"
    _SUBTITLE = "Transit random note into chord"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns exercise """
        if guitar["kind"] != "instrument":
            return None
        random_steps = []

        random_chords = Chord().get_random_chords(quantity)
        key_signature = KeySignature()

        for chord in random_chords:
            try:
                note = key_signature.get_random_relative_note(chord)
            except Exception:
                continue

            random_step = ExerciseStep(f"{note} -> {chord}")
            random_steps.append(random_step)

        output = Exercise(self._TITLE,
                          self._SUBTITLE,
                          random_steps,
                          practice_category=self.category)

        return output
