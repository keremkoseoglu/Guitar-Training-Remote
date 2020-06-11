""" Exercise module """
from enum import Enum
from typing import List

class ExerciseHelperType(Enum):
    """ Defines an exercise helper type
    Examples: open browser, start metronome, etc """
    BROWSER = 1


class ExerciseHelper:
    """ Defines an exercise helper """
    def __init__(self, helper_type: ExerciseHelperType, params: {}=None):
        self.helper_type = helper_type
        if params is None:
            self.params = {}
        else:
            self.params = params


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
