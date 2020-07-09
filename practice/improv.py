""" Improv """
import random
from copy import deepcopy
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from config import get_configuration, get_storage, save_storage


class Improv(AbstractPractice):
    """ Improv """

    _TITLE = "Improv"
    _SUBTITLE = "Practice the improv approaches"

    def __init__(self):
        self._config = get_configuration()

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns improv exercises """

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
        output.helpers = [
            ExerciseHelper(
                ExerciseHelperType.BROWSER,
                {"url": self._get_random_backing_track_url()}
            )
        ]
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

    def _get_random_backing_track_url(self) -> str:
        storage = get_storage()
        while True:
            track_index = random.randint(0, len(self._config["backing_tracks"])-1)
            track_url = self._config["backing_tracks"][track_index]
            if track_url == storage["last_improv_url"]:
                continue
            storage["last_improv_url"] = track_url
            save_storage(storage)
            return track_url
