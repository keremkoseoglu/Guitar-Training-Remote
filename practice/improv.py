""" Improv """
import random
from copy import deepcopy
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from config import get_configuration


class Improv(AbstractPractice):
    """ Improv """

    _TITLE = "Improv"
    _SUBTITLE = "Practice the improv approaches"

    def __init__(self):
        self._config = get_configuration()

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns improv exercises """
        if guitar["kind"] != "instrument":
            return None

        random_steps = []
        improvs = []

        for quantity_pos in range(0, quantity): # pylint: disable=W0612
            if len(improvs) <= 0:
                improvs = self._config["improvs"].copy()

            try:
                random_index = random.randint(0, len(improvs) - 1)
            except Exception:
                break

            random_main_improv = improvs.pop(random_index)
            sub_txt = ""

            sub_appended = False
            for one_two in range(2): # pylint: disable=W0612
                if len(improvs) == 0:
                    break
                if sub_txt == "":
                    sub_txt += "followed by "
                if len(improvs) == 1:
                    random_index = 0
                else:
                    random_index = random.randint(0, len(improvs) - 1)
                random_sub_improv = improvs.pop(random_index)
                if sub_appended:
                    sub_txt += ", "
                else:
                    sub_appended = True
                sub_txt += random_sub_improv

            random_step = exercise_step.ExerciseStep(random_main_improv, sub_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        flukebox_helper = self._get_flukebox_helper()
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

    def _get_flukebox_helper(self) -> ExerciseHelper:
        if "flukebox" not in self._config:
            return None
        command = "cd " + self._config["flukebox"]["path"] + ";"
        command += " venv/bin/python3 main.py playlist="
        command += self._config["flukebox"]["playlist"]
        output = ExerciseHelper(
            ExerciseHelperType.OS_COMMAND,
            {"command": command})
        return output
