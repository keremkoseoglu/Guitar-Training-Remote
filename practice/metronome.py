from model import exercise, exercise_step
from model.guitar import Guitar
from practice import abstract_practice
import random


class Metronome(abstract_practice.AbstractPractice):

    _TITLE = "Metronome"

    _BPM_RANGE = [60, 160]

    _METRONOME_EXERCISES = ["Random mute",
                            "Reducing in half",
                            "Count 5 over 4",
                            "1- 2- 3- 4-",
                            "1- 3-",
                            "2- 4-",
                            "1+ 2+ 3+ 4+",
                            "1+ 3+",
                            "2+ 4+",
                            "1+",
                            "2+",
                            "3+",
                            "4+",
                            "1-",
                            "2-",
                            "3-",
                            "4-"]

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:

        random_steps = []

        while len(random_steps) < quantity:
            random_exercise = self._get_random_metronome_exercise()
            random_bpm = self._get_random_bpm()
            if len(random_exercise) <= 5 and \
                    (random_exercise[:1] == "1" or
                     random_exercise[:1] == "2" or
                     random_exercise[:1] == "3" or
                     random_exercise[:1] == "4") and \
                    random_bpm > 100:
                random_bpm = round(random_bpm / 2)
            random_step = exercise_step.ExerciseStep(random_exercise, "BPM: " + str(random_bpm))
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, "Run the following exercise", random_steps)
        return output

    def _get_random_bpm(self) -> int:
        return random.randint(self._BPM_RANGE[0], self._BPM_RANGE[1])

    def _get_random_metronome_exercise(self) -> str:
        random_metronome_index = random.randint(0, len(self._METRONOME_EXERCISES) - 1)
        return self._METRONOME_EXERCISES[random_metronome_index]
