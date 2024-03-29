""" Scale dexterity """
import random
from model import exercise, exercise_step
from music_theory import scale
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory


class ScaleDexterity(AbstractPractice):
    """ Scale dexterity """
    _TITLE = "Scale dexterity"
    _SUBTITLE = "Play a scale"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns exercise """
        if guitar["kind"] != "instrument":
            return None
        random_steps = []
        random_scales = scale.Scale().get_random_scales(quantity)

        for random_scale in random_scales:

            # Build random secondary text
            if random.randint(0, 1) == 0:
                secondary_text = AbstractPractice.get_random_position_suggestion_text() # pylint: disable=C0301
            else:
                secondary_text = "Play at least 2 octaves"

            # Add step
            random_step = exercise_step.ExerciseStep(random_scale, secondary_text)
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE, ScaleDexterity._get_scale_exercise(guitar),
            random_steps, practice_category=self.category)
        return output

    @staticmethod
    def _get_scale_exercise(guitar: dict) -> str:
        scale_exercises = [
            "Play a simple scale",
            "Play at least 2 octaves"
        ]

        if guitar["strings"] > 0:
            scale_exercises.append("Play scale - all strings / positions / fingers")

        random_index = random.randint(0, len(scale_exercises) - 1)
        return scale_exercises[random_index]
