import random


class Position:

    _MAX_POSITION = 7

    def __init__(self):
        pass

    def get_random_position(self) -> str:
        return random.randint(1, self._MAX_POSITION)
