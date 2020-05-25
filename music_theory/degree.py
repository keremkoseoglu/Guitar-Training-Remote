""" Degree module """
import random


class Degree:
    """ Degree class """

    _OCTAVE_LIMIT = 7

    def __init__(self):
        self._degrees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

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
