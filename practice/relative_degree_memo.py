from model import exercise, exercise_step
from music_theory import degree, mode
from practice import abstract_practice


class RelativeDegreeModeMemo(abstract_practice.AbstractPractice):

    _TITLE = "Relative degree memo"
    _SUBTITLE = "Tell the following degree"

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        random_steps = []

        random_degrees = degree.Degree().get_random_degrees(quantity)
        random_scales_1 = mode.Mode().get_random_modes(quantity, with_note=False)
        random_scales_2 = mode.Mode().get_random_modes(quantity, with_note=False)

        for i in range(quantity):
            random_step = exercise_step.ExerciseStep(random_scales_1[i][:3] + " " + str(random_degrees[i]) + " = " + random_scales_2[i][:3] + " ?", "follow by playing on fretboard")
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
