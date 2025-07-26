""" 16th note ghost note motor """
from model import exercise, exercise_step
from model.exercise_helper import get_flukebox_helper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from config import get_configuration

class GhostNote16thMotor(AbstractPractice):
    """ 16th note ghost note motor """
    _TITLE = "16th Ghost Note Motor"
    _SUBTITLE = "Play song with 16th ghost notes"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.RIGHT_HAND

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns improv exercises """
        if not (guitar["kind"] == "instrument" and guitar["strings"] > 0):
            return None

        random_step = exercise_step.ExerciseStep("Pick random song", "in FlukeBox")
        random_steps = [random_step]

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        flukebox_helper = get_flukebox_helper("final_playlist", no_local=True)
        if flukebox_helper is not None:
            output.helpers = [flukebox_helper]
        return output
