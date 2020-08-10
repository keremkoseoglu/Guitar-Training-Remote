""" Exercise helper module """
from enum import Enum

class ExerciseHelperType(Enum):
    """ Defines an exercise helper type
    Examples: open browser, start metronome, etc """
    BROWSER = 1
    METRONOME = 2
    OS_COMMAND = 3
    BUTTONS = 4


class ExerciseHelper:
    """ Defines an exercise helper """
    def __init__(self, helper_type: ExerciseHelperType, params: {}=None):
        self.helper_type = helper_type
        if params is None:
            self.params = {}
        else:
            self.params = params
