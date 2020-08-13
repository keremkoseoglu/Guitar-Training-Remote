""" Exercise module """
from typing import List
from model.exercise_helper import ExerciseHelper
from practice.practice_category import PracticeCategory


class Exercise:
    """ Exercise class """

    def __init__(self, # pylint: disable=R0913
                 title: str,
                 description: str,
                 steps=None,
                 helpers: List[ExerciseHelper] = None,
                 practice_category: PracticeCategory = PracticeCategory.UNDEFINED):
        self.title = title
        self.description = description
        self.practice_category = practice_category

        if steps is None:
            self.steps = []
        else:
            self.steps = steps

        if helpers is None:
            self.helpers = []
        else:
            self.helpers = helpers
