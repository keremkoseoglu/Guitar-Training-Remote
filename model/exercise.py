""" Exercise module """
from dataclasses import dataclass
from typing import List
from model.exercise_helper import ExerciseHelper
from practice.practice_category import PracticeCategory


@dataclass
class Exercise:
    """ Exercise class """
    title: str
    description: str
    steps: List = None
    helpers: List[ExerciseHelper] = None
    practice_category: PracticeCategory = PracticeCategory.UNDEFINED

    def __post_init__(self):
        if self.steps is None:
            self.steps = []
        if self.helpers is None:
            self.helpers = []
