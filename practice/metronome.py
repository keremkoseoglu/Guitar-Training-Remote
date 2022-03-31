""" Metronome """
import random
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper, get_external_metronome_helper
from practice import abstract_practice
from practice.practice_category import PracticeCategory
from config import get_configuration


class Metronome(abstract_practice.AbstractPractice):
    """ Metronome """

    _TITLE = "Metronome"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.PERFORMANCE

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns metronome exercises """
        random_steps = []

        while len(random_steps) < quantity:
            random_dict = self._get_random_metronome_exercise()
            random_exercise = random_dict["exercise"]
            random_bpm = self._get_adjusted_random_bpm(random_dict)

            sub_text = f'{"External BPM:" if random_dict["external"] else "Internal BPM:"}' \
                       f' {str(random_bpm)}'

            random_step = exercise_step.ExerciseStep(random_exercise, sub_text)

            if random_dict["external"]:
                helper = get_external_metronome_helper(random_bpm)
            else:
                helper = ExerciseHelper(ExerciseHelperType.METRONOME,
                                        {"bpm": random_bpm})

            random_step.helpers = [helper]
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE,
                                   "Run the following exercise",
                                   random_steps,
                                   practice_category=self.category)

        return output

    def get_random_bpm(self) -> int:
        """ Returns a random BPM value """
        return random.randint(self._config["bpm_range"][0], self._config["bpm_range"][1])

    def _get_adjusted_random_bpm(self, random_dict: dict) -> int:
        """ Returns adjusted random BPM value """
        random_bpm = self.get_random_bpm()
        random_exercise = random_dict["exercise"]

        if len(random_exercise) <= 5 and \
                (random_exercise[:1] == "1" or
                 random_exercise[:1] == "2" or
                 random_exercise[:1] == "3" or
                 random_exercise[:1] == "4") and \
                random_bpm > 100:
            random_bpm = round(random_bpm / 2)

        if random_dict["external"]:
            if random_dict["zero_mod"] == 0:
                if random_bpm < self._config["metronome_app"]["min"]:
                    random_bpm = self._config["metronome_app"]["min"]
                if random_bpm > self._config["metronome_app"]["max"]:
                    random_bpm = self._config["metronome_app"]["max"]
            else:
                min_bpm = self._config["metronome_app"]["min"] * random_dict["zero_mod"]
                if random_bpm < min_bpm:
                    random_bpm += min_bpm
                while random_bpm % random_dict["zero_mod"] != 0:
                    random_bpm += 1
                if random_bpm > self._config["metronome_app"]["max"]:
                    random_bpm = self._config["metronome_app"]["max"]
        else:
            if random_dict["zero_mod"] != 0:
                while random_bpm % random_dict["zero_mod"] != 0:
                    random_bpm += 1

        return random_bpm

    def _get_random_metronome_exercise(self) -> str:
        random_metronome_index = random.randint(0, len(self._config["metronome_exercises"]) - 1)
        return self._config["metronome_exercises"][random_metronome_index]
