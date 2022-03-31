""" Exercise step """
from dataclasses import dataclass
from typing import List
from model.exercise_helper import ExerciseHelper

@dataclass
class ExerciseStep:
    """ Exercise step """
    main_text: str
    sub_text: str = ""
    helpers: List[ExerciseHelper] = None

    def __post_init__(self):
        if self.helpers is None:
            self.helpers = []
