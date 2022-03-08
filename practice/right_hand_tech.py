""" Right hand technique """
from model import exercise_step, exercise
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.metronome import Metronome
from practice.practice_category import PracticeCategory
import technique.right_hand

class RightHandTech(AbstractPractice):
    """ Right hand technique """

    _TITLE = "Right hand"
    _SUBTITLE = "Practice right hand techniques"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.RIGHT_HAND

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns right hand technique exercises """
        if guitar["strings"] <= 0:
            return None

        steps = []
        metronome = Metronome()
        tech = technique.right_hand.RightHand().get_random_techniques(quantity)
        for tech_pos in range(0, len(tech)):
            new_step = exercise_step.ExerciseStep(tech[tech_pos], "")

            random_bpm = metronome.get_random_bpm()
            new_step.helpers = [ExerciseHelper(ExerciseHelperType.METRONOME,
                                               {"bpm": random_bpm})]

            steps.append(new_step)

        return exercise.Exercise(self._TITLE,
                                 self._SUBTITLE,
                                 steps,
                                 practice_category=self.category)
