""" Artificial Octave """
from copy import deepcopy
from random import randint
from model import exercise
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from factory.all_practices import AllPractices


class ArtificialOctave(AbstractPractice):
    """ Artificial octave """
    _TITLE = "Artificial octave"
    _DESCRIPTION = " with artificial octaves"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns anchor note exercise """
        if guitar["kind"] != "instrument":
            return None

        output = exercise.Exercise(ArtificialOctave._TITLE, ArtificialOctave._DESCRIPTION)

        all_practices = AllPractices().get_workout(guitar=guitar, exclude_classes=["ArtificialOctave"])
        all_exercises = all_practices.exercises
        random_index = randint(0, len(all_exercises) - 1)
        random_exercise = all_exercises.pop(random_index)
        output = deepcopy(random_exercise)
        output.title += " " + ArtificialOctave._TITLE
        output.description += " " + ArtificialOctave._DESCRIPTION

        return output
