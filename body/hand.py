""" Module for human hand """
from typing import List
from copy import copy
from random import randint

class Finger:
    """ Finger class """
    def __init__(self, number: int, name: str):
        self.number = number
        self.name = name

class Hand:
    """ Hand class """
    def __init__(self):
        self.fingers = [
            Finger(1, "Index"),
            Finger(2, "Middle"),
            Finger(3, "Ring"),
            Finger(4, "Pinky"),
            Finger(5, "Thumb")
        ]

    def get_random_fret_fingers(self, quantity: int = 0) -> List[Finger]:
        """ Returns a random list of fretting fingers """
        output = []
        candidates = self._get_fret_fingers()

        if quantity > 0:
            output_quantity = quantity
        else:
            output_quantity = randint(0, len(candidates)-1)

        while len(output) < output_quantity and len(candidates) > 0:
            random_index = randint(0, len(candidates)-1)
            random_finger = candidates.pop(random_index)
            output.append(random_finger)

        return output

    def get_random_fret_finger_permutation(self) -> List[Finger]:
        """ Returns a single finger permutation """
        output = []
        fret_fingers = self._get_fret_fingers()
        while len(fret_fingers) > 0:
            random_index = randint(0, len(fret_fingers)-1)
            random_finger = fret_fingers.pop(random_index)
            output.append(random_finger)
        return output

    def get_random_fret_finger_permutations(self, count: int) -> List[List[Finger]]:
        """ Returns a list of finger permutations """
        output = []
        while len(output) < count:
            random_permutation = self.get_random_fret_finger_permutation()
            if random_permutation not in output:
                output.append(random_permutation)
        return output

    def _get_fret_fingers(self) -> List[Finger]:
        output = copy(self.fingers)
        output.pop(4)
        return output
