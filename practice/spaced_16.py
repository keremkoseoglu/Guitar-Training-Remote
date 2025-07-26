""" Spaced 16th pattern """
import random
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from config import get_configuration


class Spaced16thPattern(AbstractPractice):
    """Spaced 16th pattern"""

    _TITLE = "Spaced 16th pattern"
    _SUBTITLE = "Play the following pattern"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.TIMING

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """Returns improv exercises"""
        random_steps = []

        for step_index in range(0, quantity):  # pylint: disable=W0612
            step_text = "XXXX"

            number_of_spaces = random.randint(1, 2)
            space_positions = random.sample(range(1, 5), number_of_spaces)

            for sp in space_positions:
                step_text = step_text[: sp - 1] + "o" + step_text[sp:]

            random_step = exercise_step.ExerciseStep(step_text)

            random_bpm = random.randint(
                self._config["bpm_range"][0], self._config["bpm_range"][1]
            )
            helper = ExerciseHelper(ExerciseHelperType.METRONOME, {"bpm": random_bpm})
            random_step.helpers = [helper]
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output
