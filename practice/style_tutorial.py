""" Style tutorial """
from model.exercise import Exercise
from model.exercise_step import ExerciseStep
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from music_theory.style import Style

class StyleTutorial(AbstractPractice):
    """ Style tutorial """
    _TITLE = "Style"
    _SUBTITLE = "Tutorial on"

    def __init__(self):
        self._style = Style()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.EDUCATION

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns random style exercise """
        return Exercise(
            self._TITLE,
            self._SUBTITLE,
            [ExerciseStep(self._style.get_random_style())],
            practice_category=self.category)
