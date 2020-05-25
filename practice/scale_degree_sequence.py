""" Scale degree sequence """
import random
from model import exercise, exercise_step
from model.guitar import Guitar
from music_theory import degree, scale
from practice import abstract_practice


class ScaleDegreeSequence(abstract_practice.AbstractPractice):
    """ Scale degree sequence """

    _TITLE = "Scale degree sequence"
    _SUBTITLE = "Play the sequence"

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:
        """ Returns scale degree sequence exercise """

        random_steps = []

        for quantity_pos in range(quantity): # pylint: disable=W0612
            random_count = random.randint(2, 7) # pylint: disable=W0612
            random_degrees = degree.Degree().get_random_degrees(7)
            sequence_txt = ""
            for random_pos in range(random_count): # pylint: disable=W0612
                if sequence_txt != "":
                    sequence_txt += ", "
                sequence_txt += str(random_degrees.pop(0))

            random_scale = scale.Scale().get_random_scale()

            random_step = exercise_step.ExerciseStep(random_scale, sequence_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
