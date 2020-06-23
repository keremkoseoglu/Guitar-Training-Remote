""" Exercise module """
from typing import List
from model.exercise_helper import ExerciseHelper


class Exercise:
    """ Exercise class """

    def __init__(self,
                 title: str,
                 description: str,
                 steps=None,
                 helpers: List[ExerciseHelper] = None):
        self.title = title
        self.description = description

        if steps is None:
            self.steps = []
        else:
            self.steps = steps

        if helpers is None:
            self.helpers = []
        else:
            self.helpers = helpers
