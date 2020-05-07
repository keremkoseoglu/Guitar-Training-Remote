from model import exercise, exercise_step
from model.guitar import Guitar
from music_theory import degree, scale
from practice import abstract_practice
import random


class ScaleDegreeSequence(abstract_practice.AbstractPractice):

    _TITLE = "Scale degree sequence"
    _SUBTITLE = "Play the sequence"

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:

        random_steps = []

        for i in range(quantity):
            random_count = random.randint(2, 7)
            random_degrees = degree.Degree().get_random_degrees(7)
            sequence_txt = ""
            for n in range(random_count):
                if sequence_txt != "":
                    sequence_txt += ", "
                sequence_txt += str(random_degrees.pop(0))

            random_scale = scale.Scale().get_random_scale()

            random_step = exercise_step.ExerciseStep(random_scale, sequence_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
