""" Position module """
import random


class Position:
    """ Position class """
    _CHORD_TONES = [1, 3, 5]
    _MAX_POSITION = 7

    def __init__(self):
        pass

    @staticmethod
    def get_random_chord_position() -> str:
        """ Returns a random chord position """
        random_index = random.randint(0, len(Position._CHORD_TONES) - 1)
        return str(Position._CHORD_TONES[random_index])

    @staticmethod
    def get_random_position() -> str:
        """ Returns a random position """
        return random.randint(1, Position._MAX_POSITION)
