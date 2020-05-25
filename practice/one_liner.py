""" One liner """
import random
from model import exercise, exercise_step
from model.guitar import Guitar
from practice.abstract_practice import AbstractPractice


class OneLiner(AbstractPractice):
    """ One liner """

    _ONE_LINERS = [
        "Old licks",
        "New lick",

        "Solo / repertoire",
        "Solo / one chord"
        "Chord melody",
        "Melody / chords",

        "Transcribe solo",
        "Transcribe groove",

        "Bebop (2 5 1)",
        "Circle of 5ths",
        "Groove loop over drum",
        "New style",
        "Repertoire",
        "Fill power trio solo",
        "YouTube lesson"
    ]

    _TITLE = "One-Liner"
    _SUBTITLE = "Go over the one-liners"

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:
        """ Returns random one liner exercises """

        random_steps = []
        one_liners = []

        for quantity_pos in range(0, quantity): # pylint: disable=W0612
            if len(one_liners) == 0:
                one_liners = self._ONE_LINERS.copy()
            random_index = random.randint(0, len(one_liners) - 1)
            random_one_liner = one_liners.pop(random_index)
            random_step = exercise_step.ExerciseStep(random_one_liner, "")
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
