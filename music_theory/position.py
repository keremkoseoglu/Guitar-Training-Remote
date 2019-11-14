import random


class Position:

    _CHORD_TONES = [1, 3, 5]
    _MAX_POSITION = 7

    def __init__(self):
        pass

    def get_random_chord_position(self) -> str:
        random_index = random.randint(0, len(Position._CHORD_TONES) - 1)
        return Position._CHORD_TONES[random_index]

    def get_random_position(self) -> str:
        return random.randint(1, self._MAX_POSITION)
