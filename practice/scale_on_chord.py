""" Scale on chord """
import random
from model import exercise, exercise_step
from music_theory import chord
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory


class ScaleOnChord(AbstractPractice):
    """ Scale on chord """
    _TITLE = "Scale on chord"
    _SUBTITLE = "a scale on top of chord"
    _PLAY_CHOICE = ["Play in", "Play out"]

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random scale on chord exercises """
        if guitar["kind"] != "instrument":
            return None
        random_steps = []
        random_chords = chord.Chord().get_random_chords(quantity)

        for random_chord in random_chords:
            random_step = exercise_step.ExerciseStep(
                random_chord,
                AbstractPractice.get_random_position_suggestion_text()
            )

            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            ScaleOnChord._get_subtitle(),
            random_steps,
            practice_category=self.category)
        return output

    @staticmethod
    def _get_random_play_choice() -> str:
        random_choice = random.randint(0, len(ScaleOnChord._PLAY_CHOICE) - 1)
        return ScaleOnChord._PLAY_CHOICE[random_choice]

    @staticmethod
    def _get_subtitle() -> str:
        return f"{ScaleOnChord._get_random_play_choice()} {ScaleOnChord._SUBTITLE}"
