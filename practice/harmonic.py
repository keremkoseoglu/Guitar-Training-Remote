""" Harmonics """
from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from music_theory import chord


class Harmonic(AbstractPractice):
    """ Harmonic """
    _TITLE = "Harmonics"
    _SUBTITLE = "Play harmonics over"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns harmonic over random chord connection exercises """
        if not (guitar["kind"] == "instrument" and guitar["strings"] > 0):
            return None

        random_steps = []
        random_chords = chord.Chord().get_random_chords(quantity)

        for random_chord in random_chords:
            random_step = exercise_step.ExerciseStep(random_chord, "")
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)
        return output
