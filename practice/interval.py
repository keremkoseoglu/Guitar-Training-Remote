""" Intervals """
import random
from model import exercise, exercise_step
from music_theory import degree, mode
from practice import abstract_practice
from practice.practice_category import PracticeCategory


class Intervals(abstract_practice.AbstractPractice):
    """ Intervals """

    _DIRECTIONS = ["Up", "Down"]
    _TITLE = "Interval practice"
    _SUBTITLE = "Play shifting intervals"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random interval exercises """
        if guitar["kind"] != "instrument":
            return None

        degree_obj = degree.Degree()
        mode_obj = mode.Mode()
        random_steps = []

        for step_index in range(0, quantity): # pylint: disable=W0612
            mode_text = f"{mode_obj.get_random_mode()} {self._get_direction()}"

            step_text = ""

            while True:
                degree_count = 2
                degrees = degree_obj.get_random_degrees(degree_count, limit_octave=True)
                if not (
                        (degree_count == 2 and degrees[0] == degrees[1])
                        or
                        (degree_count == 2 and abs(degrees[1] - degrees[0]) == 1)
                ):
                    break

            for deg in degrees:
                if step_text != "":
                    step_text += ", "
                step_text += str(deg)

            random_step = exercise_step.ExerciseStep(mode_text, sub_text=step_text)
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output

    def _get_direction(self) -> str:
        dir_index = random.randint(0, len(self._DIRECTIONS) - 1)
        return self._DIRECTIONS[dir_index]
