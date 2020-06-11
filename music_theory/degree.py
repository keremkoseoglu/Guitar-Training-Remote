""" Degree module """
import random
from config import get_configuration


class Degree:
    """ Degree class """

    _OCTAVE_LIMIT = 7

    def __init__(self):
        config = get_configuration()
        self._degrees = config["degrees"]

    def get_random_degree(self, limit_octave=False) -> int:
        """ Returns a random degree """
        while True:
            i = random.randint(0, len(self._degrees) - 1)
            degree = self._degrees[i]
            if limit_octave:
                if degree <= self._OCTAVE_LIMIT:
                    return degree
            else:
                return degree

    def get_random_degrees(self, count: int, limit_octave=False) -> []:
        """ Returns random degrees """
        output = []

        for range_pos in range(count): # pylint: disable=W0612
            random_degree = self.get_random_degree(limit_octave=limit_octave)
            output.append(random_degree)

        return output
