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
        "Simple melody",
        "Chromatic",
        "Repeating elements",
        "Chords",
        "Distant notes",
        "Close notes",
        "Bebop",
        "Blockbuster",
        "Feeling projection",
        "Emotion graph",

        "Play out - mel.min.",
        "Play out - chromatic",
        "Coltrane patterns",
        "Phrasing",
        "Rhythmic games",
        "Right target note",
        "Strong beat / note",
        "Double stops",
        "Thematic improv",
        "Call & response",
        "Emphasize chords",

        "Dom7 phrygian",
        "Dom7 altered",
        "Dom7 3rd Dim",

        "Free lyric solo",
        "Mindful of rhythm / harm / melody",
        "Emphasize chord tones",
        "Start end on chord tones",
        "Play the silence",
        "Whole tone",
        "Accents"
    ]

    _TITLE = "Improv"
    _SUBTITLE = "Practice the improv approaches"

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        random_steps = []
        improvs = []

        for i in range(0, quantity):
            if len(improvs) <= 0:
                improvs = self._IMPROVS.copy()

            try:
                random_index = random.randint(0, len(improvs) - 1)
            except:
                break

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

    def get_improvs(self) -> []:
        return self._IMPROVS

    def get_improvs(self, count: int) -> []:
        output = []

        improvs = self._IMPROVS
        for r in range(count):
            if len(improvs) <= 0:
                break
            i = random.randint(0, len(improvs) - 1)
            output.append(improvs.pop(i))

        return output
