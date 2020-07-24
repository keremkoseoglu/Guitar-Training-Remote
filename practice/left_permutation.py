""" Left hand permutations module """
from random import randint
from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
from body.hand import Hand
from config import get_configuration

class LeftFingerPermutations(AbstractPractice):
    """ Finger permutation class """

    _TITLE = "Fret finger permutations"
    _SUBTITLE = "Wander strings with the following"
    _AT_LEAST = 1

    def __init__(self):
        self._config = get_configuration()

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns lazy fingers exercises """
        if guitar["kind"] != "instrument":
            return None
        string_count = guitar["strings"]
        if string_count <= 0:
            return None

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
            random_step = exercise_step.ExerciseStep(
                "Follow",
                sub_text=permutation_text)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
