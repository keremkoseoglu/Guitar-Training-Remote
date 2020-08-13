""" Voice """
from model import exercise, exercise_step
from practice import abstract_practice
from practice.practice_category import PracticeCategory

class Voice(abstract_practice.AbstractPractice):
    """ Voice """
    _TITLE = "Voice Pitch"
    _SUBTITLE = "Do voice pitch exercises"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns voice exercise """
        if guitar["kind"] != "voice":
            return None
        step = exercise_step.ExerciseStep("Pick phone", "Use app")

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            [step],
            practice_category=self.category)

        return output
