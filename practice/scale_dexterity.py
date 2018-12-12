from model import exercise, exercise_step
from music_theory import scale
from practice import abstract_practice


class ScaleDexterity(abstract_practice.AbstractPractice):

    _TITLE = "Scale dexterity"
    _SUBTITLE = "Play a scale"

    def get_exercise(self, quantity: int) -> exercise.Exercise:
        random_steps = []

        random_scales = scale.Scale().get_random_scales(quantity)

        for random_scale in random_scales:
            random_step = exercise_step.ExerciseStep(random_scale,
                                                     super(ScaleDexterity, self).get_random_position_suggestion_text())
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
