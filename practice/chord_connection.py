from model import exercise, exercise_step
from practice import abstract_practice, improv
from music_theory import chord
import random


class ChordConnection(abstract_practice.AbstractPractice):
    _TITLE = "Chord Connection"
    _SUBTITLE = "Connect chords via"

    def get_exercise(self, quantity: int) -> exercise.Exercise:
        random_steps = []

        for random_improv in improv.Improv().get_improvs(quantity):
            context_count = random.randint(2, 4)
            stuff = chord.Chord().get_random_chords(context_count)

            stuff_txt = ""
            for s in stuff:
                if stuff_txt != "":
                    stuff_txt += " | "
                stuff_txt += s

            random_step = exercise_step.ExerciseStep(random_improv, stuff_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
