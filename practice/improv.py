from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
import random

class Improv(AbstractPractice):

    _IMPROVS = [
        "Tonal / modal",
        "2 5 1 lick",
        "3/5 note phrasing",
        "Random note",
        "Approach note",
        "Sequence",
        "Tritone sub",
        "Tritone sub (Lyd b7)",
        "Dom7 3rd Dim",
        "Half step above",
        "Simple melody",
        "Chromatic",
        "Repetition",
        "Chords",
        "Distant notes",
        "Two threes maj",
        "Bebop",
        "Blockbuster",
        "Feeling projection"
    ]

    _TITLE = "Improv"
    _SUBTITLE = "Practice the improv approaches"

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        random_steps = []
        improvs = []

        for i in range(0, quantity):
            if len(improvs) == 0:
                improvs = self._IMPROVS.copy()
            random_index = random.randint(0, len(improvs) - 1)
            random_main_improv = improvs.pop(random_index)
            sub_txt = ""

            sub_appended = False
            for i in range(2):
                if len(improvs) == 0:
                    break
                if sub_txt == "":
                    sub_txt += "followed by "
                if len(improvs) == 1:
                    random_index = 0
                else:
                    random_index = random.randint(0, len(improvs) - 1)
                random_sub_improv = improvs.pop(random_index)
                if sub_appended:
                    sub_txt += ", "
                else:
                    sub_appended = True
                sub_txt += random_sub_improv

            random_step = exercise_step.ExerciseStep(random_main_improv, sub_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
