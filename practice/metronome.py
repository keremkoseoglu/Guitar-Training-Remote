""" Metronome """
import random
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
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
            random_exercise = self._get_random_metronome_exercise()
            random_bpm = self.get_random_bpm()
            if len(random_exercise) <= 5 and \
                    (random_exercise[:1] == "1" or
                     random_exercise[:1] == "2" or
                     random_exercise[:1] == "3" or
                     random_exercise[:1] == "4") and \
                    random_bpm > 100:
                random_bpm = round(random_bpm / 2)
            random_step = exercise_step.ExerciseStep(random_exercise, "BPM: " + str(random_bpm))
            random_step.helpers = [ExerciseHelper(
                ExerciseHelperType.METRONOME,
                {"bpm": random_bpm}
            )]
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            "Run the following exercise",
            random_steps,
            practice_category=self.category)

        return output

    def get_random_bpm(self) -> int:
        """ Returns a random BPM value """
        return random.randint(self._config["bpm_range"][0], self._config["bpm_range"][1])

    def _get_random_metronome_exercise(self) -> str:
        random_metronome_index = random.randint(0, len(self._config["metronome_exercises"]) - 1)
        return self._config["metronome_exercises"][random_metronome_index]
