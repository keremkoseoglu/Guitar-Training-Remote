""" Exercise step """
from typing import List
from model.exercise_helper import ExerciseHelper

class ExerciseStep:
    """ Exercise step """
    def __init__(self, main_text: str, sub_text: str = "", helpers: List[ExerciseHelper] = None):
        self.main_text = main_text
        self.sub_text = sub_text


        if helpers is None:
            self.helpers = []
        else:
            self.helpers = helpers
