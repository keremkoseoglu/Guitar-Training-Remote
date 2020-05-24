from model import exercise_step, exercise
from model.guitar import Guitar
from practice.abstract_practice import AbstractPractice
import technique.right_hand

class RightHandTech(AbstractPractice):

    _TITLE = "Right hand"
    _SUBTITLE = "Practice right hand techniques"

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:
        if guitar != Guitar.BASS:
            return None

        steps = []
        tech = technique.right_hand.RightHand().get_random_techniques(quantity)
        for i in range(0, len(tech)):
            new_step = exercise_step.ExerciseStep(tech[i], "")
            steps.append(new_step)
        return exercise.Exercise(self._TITLE, self._SUBTITLE, steps)

