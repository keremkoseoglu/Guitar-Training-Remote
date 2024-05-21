""" Finger independence
This module contains exercises for left hand fingers
"""

from random import randint
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome
from body.hand import Hand


class FingerIndependence(AbstractPractice):
    """Finger independence class"""

    _TITLE = "Finger independence"
    _SUBTITLE = "Play sequence, moving some fingers"

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.LEFT_HAND

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """Returns lazy fingers exercises"""
        if guitar["kind"] != "instrument":
            return None

        string_count = guitar["strings"]
        if string_count <= 0:
            return None

        metronome = Metronome()
        random_steps = []
        hand = Hand()

        for quantity_pos in range(quantity):  # pylint: disable=W0612
            finger_perms = hand.get_random_fret_finger_permutation(
                allow_duplicates=False
            )
            moveable_finger_count = randint(1, 3)
            movable_fingers = hand.get_random_fret_fingers(moveable_finger_count)

            fingers_str = ""
            for finger in finger_perms:
                is_movable = False
                for mv in movable_fingers:
                    if mv.number == finger.number:
                        is_movable = True
                        break
                finger_str = ""
                if is_movable:
                    finger_str = f"({finger.number})"
                else:
                    finger_str = f"{finger.number}"
                if fingers_str != "":
                    fingers_str += " "
                fingers_str += finger_str

            random_bpm = metronome.get_random_bpm()

            random_step = exercise_step.ExerciseStep(
                f"{str(random_bpm)} bpm", fingers_str
            )

            random_step.helpers = [
                ExerciseHelper(ExerciseHelperType.METRONOME, {"bpm": random_bpm})
            ]

            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output
