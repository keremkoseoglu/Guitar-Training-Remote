""" Repertoir transcription (original riffs) """
from model import exercise, exercise_step
from model.exercise_helper import get_flukebox_helper
from practice.practice_category import PracticeCategory
from config import get_configuration


class TranscribeRepertoirAsOriginal():
    """ Repertoir transcription (original riffs)
    PROTOCOL: AbstractPractice
    """

    _TITLE = "Transcribe rep."
    _SUBTITLE = "Transcribe songs as original"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.EDUCATION

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns improv exercises """
        if guitar["kind"] != "instrument":
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
