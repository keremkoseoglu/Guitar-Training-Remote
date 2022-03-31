""" Lazy fingers module
This module contains exercises for left hand fingers 2, 3, 4
"""
from random import randint
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome
from body.hand import Hand


class LazyFingers(AbstractPractice):
    """ Lazy fingers exercise class """

    _TITLE = "Lazy fingers"
    _SUBTITLE = "Work your lazy fingers"
    _MAX_STRING_JUMP = 2

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.LEFT_HAND

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns lazy fingers exercises """
        if guitar["kind"] != "instrument":
            return None

        string_count = guitar["strings"]
        if string_count <= 0:
            return None

        metronome = Metronome()
        random_steps = []

        for quantity_pos in range(quantity): # pylint: disable=W0612
            random_finger_count = randint(2, 4)
            random_fingers = Hand().get_random_fret_fingers(random_finger_count)
            strings = []
            fingers = []
            prev_rand_string = -1

            while len(random_fingers) > 0:
                random_finger_index = randint(0, len(random_fingers)-1)
                random_finger = random_fingers.pop(random_finger_index)
                fingers.append(random_finger)

                while True:
                    random_string = randint(1, string_count)
                    if prev_rand_string == -1:
                        break
                    string_jump = abs(random_string - prev_random_string)
                    if string_jump <= LazyFingers._MAX_STRING_JUMP:
                        break

                prev_random_string = random_string
                strings.append(random_string)

            sorted(strings, key=lambda string: string)
            sorted(fingers, key=lambda finger: finger.number)

            pattern = ""
            for pattern_index in range(len(strings)):
                if pattern != "":
                    pattern += " "
                pattern += "S" + str(strings[pattern_index])
                pattern += "  " + fingers[pattern_index].name

            random_bpm = metronome.get_random_bpm()

            random_step = exercise_step.ExerciseStep(
                f"{str(random_bpm)} bpm",
                pattern)

            random_step.helpers = [ExerciseHelper(
                ExerciseHelperType.METRONOME,
                {"bpm": random_bpm})]

            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output
