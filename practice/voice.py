""" Voice """
from model import exercise, exercise_step
from practice import abstract_practice

class Voice(abstract_practice.AbstractPractice):
    """ Voice """
    _TITLE = "Voice Pitch"
    _SUBTITLE = "Do voice pitch exercises"

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns voice exercise """
        if guitar["kind"] != "voice":
            return None
        step = exercise_step.ExerciseStep("Pick phone", "Use app")
        output = exercise.Exercise(self._TITLE, self._SUBTITLE, [step])
        return output
