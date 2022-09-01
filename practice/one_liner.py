""" One liner """
import random
from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from config import get_configuration
from performance.advice import Advice

class OneLiner(AbstractPractice):
    """ One liner """
    _TITLE = "One-Liner"
    _SUBTITLE = "Go over the one-liners"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.EDUCATION

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random one liner exercises """
        if guitar["kind"] != "instrument":
            return None
        random_steps = []
        one_liners = []

        for quantity_pos in range(0, quantity): # pylint: disable=W0612
            if len(one_liners) == 0:
                one_liners = self._config["one_liners"].copy()
            random_index = random.randint(0, len(one_liners) - 1)
            random_one_liner = one_liners.pop(random_index)
            random_step = exercise_step.ExerciseStep(random_one_liner, Advice().get_random_advice())
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output
