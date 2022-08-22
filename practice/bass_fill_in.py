""" Bass fill in module """
from config import get_configuration
from model.exercise import Exercise
from model.exercise_step import ExerciseStep
from model.exercise_helper import get_flukebox_helper, ExerciseHelper, ExerciseHelperType
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory

class BassFillIn(AbstractPractice):
    """ Bass fill in """
    _TITLE = "Bass fill in"
    _SUBTITLE = "Apply bass fill in"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.PERFORMANCE

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns exercise """
        if guitar["kind"] != "instrument":
            return None

        dummy_step = ExerciseStep(BassFillIn._SUBTITLE)

        output = Exercise(
            self._TITLE,
            self._SUBTITLE,
            [dummy_step],
            practice_category=self.category)

        flukebox_helper = get_flukebox_helper("final_playlist")
        if flukebox_helper is not None:
            if output.helpers is None:
                output.helpers = []
            output.helpers.append(flukebox_helper)

        config = get_configuration()
        browser_helper = ExerciseHelper(ExerciseHelperType.BROWSER)
        browser_helper.params["url"] = config["bass_fill_url"]
        output.helpers.append(browser_helper)

        return output
