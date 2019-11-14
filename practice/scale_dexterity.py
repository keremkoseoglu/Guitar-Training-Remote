from model import exercise, exercise_step
from music_theory import scale
from practice import abstract_practice
import random

class ScaleDexterity(abstract_practice.AbstractPractice):

    _TITLE = "Scale dexterity"

    _SCALE_EXERCISES = [
        "Play a simple scale",
        "Play at least 2 octaves",
        "Play scale - all strings / positions / fingers"
    ]

    _SUBTITLE = "Play a scale"

    def get_exercise(self, quantity: int) -> exercise.Exercise:
        random_steps = []

        random_scales = scale.Scale().get_random_scales(quantity)

        for random_scale in random_scales:

            # Build random secondary text
            if random.randint(0, 1) == 0:
                secondary_text = super(ScaleDexterity, self).get_random_position_suggestion_text()
            else:
                secondary_text = "Play at least 2 octaves"

            # Add step
            random_step = exercise_step.ExerciseStep(random_scale, secondary_text)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._get_scale_exercise(), random_steps)
        return output

    def _get_scale_exercise(self) -> str:
        random_index = random.randint(0, len(self._SCALE_EXERCISES) - 1)
        return self._SCALE_EXERCISES[random_index]
