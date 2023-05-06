""" Fingers 2, 3, 4 """
from copy import deepcopy
from random import randint
from model import exercise
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from factory.all_practices import AllPractices


class Fingers234(AbstractPractice):
    """ Fingers 2, 3, 4 """
    _TITLE = "Fingers 234"
    _DESCRIPTION = " with fingers 2 3 4 only"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns anchor note exercise """
        if guitar["kind"] != "instrument":
            return None

        output = exercise.Exercise(Fingers234._TITLE, Fingers234._DESCRIPTION)

        all_practices = AllPractices().get_workout(guitar=guitar, exclude_classes=["Fingers234"])
        all_exercises = all_practices.exercises
        random_index = randint(0, len(all_exercises) - 1)
        random_exercise = all_exercises.pop(random_index)
        output = deepcopy(random_exercise)
        output.title += " " + Fingers234._TITLE
        output.description += " " + Fingers234._DESCRIPTION

        return output
