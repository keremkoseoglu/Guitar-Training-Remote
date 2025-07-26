""" Improv """
import random
from copy import deepcopy
from model import exercise, exercise_step
from model.exercise_helper import get_flukebox_helper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from config import get_configuration
from performance.advice import Advice

class Improv(AbstractPractice):
    """ Improv """
    _TITLE = "Improv"
    _SUBTITLE = "Practice the improv approaches"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.PERFORMANCE

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns improv exercises """
        if guitar["kind"] != "instrument":
            return None

        random_steps = []
        improvs = []
        advice = Advice()

        for quantity_pos in range(0, quantity): # pylint: disable=W0612
            if len(improvs) <= 0:
                improvs = self._config["improvs"].copy()

            try:
                random_index = random.randint(0, len(improvs) - 1)
            except Exception:
                break

            random_main_improv = improvs.pop(random_index)
            sub_txt = advice.get_random_advice()
            random_step = exercise_step.ExerciseStep(random_main_improv, sub_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        flukebox_helper = get_flukebox_helper("backing_playlist")
        if flukebox_helper is not None:
            output.helpers = [flukebox_helper]
        return output

    def get_improvs(self, count: int) -> []:
        """ Returns a random number of improv exercises """
        output = []

        improvs = deepcopy(self._config["improvs"])
        for count_pos in range(count): # pylint: disable=W0612
            if len(improvs) <= 0:
                break
            i = random.randint(0, len(improvs) - 1)
            output.append(improvs.pop(i))

        return output
