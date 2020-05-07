from model import exercise, exercise_step
from model.guitar import Guitar
from music_theory import scale
from practice import abstract_practice
import random

class ScaleDexterity(abstract_practice.AbstractPractice):

    _TITLE = "Scale dexterity"
    _SUBTITLE = "Play a scale"

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:
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

        output = exercise.Exercise(self._TITLE, self._get_scale_exercise(guitar), random_steps)
        return output

    def _get_scale_exercise(self, guitar: Guitar) -> str:
        scale_exercises = [
            "Play a simple scale",
            "Play at least 2 octaves"
        ]

        if guitar != Guitar.KEYS:
            scale_exercises.append("Play scale - all strings / positions / fingers")

        random_index = random.randint(0, len(scale_exercises) - 1)
        return scale_exercises[random_index]
