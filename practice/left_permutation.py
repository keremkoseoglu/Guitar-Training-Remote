"""Left hand permutations module"""

from random import randint
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from model.guitar import get_random_fret
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome
from body.hand import Hand
from config import get_configuration


class LeftFingerPermutations(AbstractPractice):
    """Finger permutation class"""

    _TITLE = "Fret finger permutations"
    _SUBTITLE = "Wander strings with the following"
    _AT_LEAST = 1

    def __init__(self):
        self._config = get_configuration()

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
        while len(random_steps) < quantity:
            permutation_count = randint(
                LeftFingerPermutations._AT_LEAST, self._config["max_left_permutation"]
            )

            duplicate_rnd = randint(0, 1)
            allow_duplicates = duplicate_rnd == 0

            permutations = hand.get_random_fret_finger_permutations(
                permutation_count, allow_duplicates=allow_duplicates
            )

            permutation_text = _build_permutation_text(permutations)
            first_fret = get_random_fret()
            random_bpm = metronome.get_random_bpm()
            random_step = exercise_step.ExerciseStep(
                f"Fret {str(first_fret)} ({str(random_bpm)} bpm)",
                sub_text=permutation_text,
            )

            random_step.helpers = [
                ExerciseHelper(ExerciseHelperType.METRONOME, {"bpm": random_bpm})
            ]

            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output


def _build_permutation_text(permutations: list) -> str:
    result = ""

    match randint(0, 2):
        case 0:
            decorator = "V"
        case 1:
            decorator = "L"
        case 2:
            decorator = ""

    for permutation in permutations:
        if result != "":
            result += " |"
        for finger in permutation:
            if decorator == "V":
                strong = "*" if randint(0, 1) == 0 else ""
            elif decorator == "L":
                strong = "L" if randint(0, 1) == 0 else ""
            else:
                strong = ""

            result += " " + strong + str(finger.number)

    return result
