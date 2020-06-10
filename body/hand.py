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
        candidates = copy(self.fingers)
        candidates.pop(4)

        if quantity > 0:
            output_quantity = quantity
        else:
            output_quantity = randint(0, len(candidates)-1)

        while len(output) < output_quantity and len(candidates) > 0:
            random_index = randint(0, len(candidates)-1)
            random_finger = candidates.pop(random_index)
            output.append(random_finger)

        return output
