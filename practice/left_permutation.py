""" Left hand permutations module """
from random import randint
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome
from body.hand import Hand
from config import get_configuration

class LeftFingerPermutations(AbstractPractice):
    """ Finger permutation class """
    _TITLE = "Fret finger permutations"
    _SUBTITLE = "Wander strings with the following"
    _AT_LEAST = 1
    _LOW_FRET = 4
    _HIGH_FRET = 12

    def __init__(self):
        self._config = get_configuration()

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
        hand = Hand()
        while len(random_steps) < quantity:
            permutation_count = randint(
                LeftFingerPermutations._AT_LEAST,
                self._config["max_left_permutation"])
            permutations = hand.get_random_fret_finger_permutations(permutation_count)
            permutation_text = ""
            for permutation in permutations:
                if permutation_text != "":
                    permutation_text += " |"
                for finger in permutation:
                    permutation_text += " " + str(finger.number)
            first_fret = LeftFingerPermutations._get_random_fret()
            random_bpm = metronome.get_random_bpm()
            random_step = exercise_step.ExerciseStep(
                f"Fret {str(first_fret)} ({str(random_bpm)} bpm)",
                sub_text=permutation_text)

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

    @staticmethod
    def _get_random_fret() -> int:
        return randint(
            LeftFingerPermutations._LOW_FRET,
            LeftFingerPermutations._HIGH_FRET)
