""" Scale on chord """
import random
from model import exercise, exercise_step

from music_theory import chord
from practice import abstract_practice


class ScaleOnChord(abstract_practice.AbstractPractice):
    """ Scale on chord """

    _TITLE = "Scale on chord"
    _SUBTITLE = "a scale on top of chord"
    _PLAY_CHOICE = ["Play in", "Play out"]

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random scale on chord exercises """

        random_steps = []
        random_chords = chord.Chord().get_random_chords(quantity)

        for random_chord in random_chords:
            random_step = exercise_step.ExerciseStep(
                random_chord,
                abstract_practice.AbstractPractice.get_random_position_suggestion_text()
            )

            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, ScaleOnChord._get_subtitle(), random_steps)
        return output

    @staticmethod
    def _get_random_play_choice() -> str:
        random_choice = random.randint(0, len(ScaleOnChord._PLAY_CHOICE) - 1)
        return ScaleOnChord._PLAY_CHOICE[random_choice]

    @staticmethod
    def _get_subtitle() -> str:
        return ScaleOnChord._get_random_play_choice() + " " + ScaleOnChord._SUBTITLE
