""" Scale without avoid notes """

from model import exercise, exercise_step
from music_theory import scale
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory


class ScaleAvoid(AbstractPractice):
    """Scale without avoid notes"""

    _TITLE = "Scale avoid"
    _SUBTITLE = "Scale without avoid notes"

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """Returns exercise"""
        if guitar["kind"] != "instrument":
            return None
        random_steps = []
        random_scales = scale.Scale().get_random_scales(quantity)

        for random_scale in random_scales:
            random_step = exercise_step.ExerciseStep(
                random_scale, "Play without avoid notes"
            )
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category,
        )
        return output
