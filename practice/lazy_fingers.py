""" Lazy fingers module
This module contains exercises for left hand fingers 2, 3, 4
"""
from random import randint
from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
from body.hand import Hand


class LazyFingers(AbstractPractice):
    """ Lazy fingers exercise class """

    _TITLE = "Lazy fingers"
    _SUBTITLE = "Work your lazy fingers"

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns lazy fingers exercises """
        random_steps = []

        string_count = guitar["strings"]
        if string_count <= 0:
            return None

        for quantity_pos in range(quantity): # pylint: disable=W0612
            random_finger_count = randint(2, 4)
            random_fingers = Hand().get_random_fret_fingers(random_finger_count)
            strings = []
            fingers = []

            while len(random_fingers) > 0:
                random_finger_index = randint(0, len(random_fingers)-1)
                random_finger = random_fingers.pop(random_finger_index)
                fingers.append(random_finger)
                random_string = randint(1, string_count)
                strings.append(random_string)

            sorted(strings, key=lambda string: string)
            sorted(fingers, key=lambda finger: finger.number)

            pattern = ""
            for pattern_index in range(len(strings)):
                if pattern != "":
                    pattern += " "
                pattern += "S" + str(strings[pattern_index])
                pattern += "  " + fingers[pattern_index].name

            random_step = exercise_step.ExerciseStep(
                "Follow",
                pattern
            )

            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output