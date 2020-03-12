import random


class Degree:
    _OCTAVE_LIMIT = 7

    def __init__(self):
        self._degrees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def get_random_degree(self, limit_octave=False) -> int:
        while True:
            i = random.randint(0, len(self._degrees) - 1)
            degree = self._degrees[i]
            if limit_octave:
                if degree <= self._OCTAVE_LIMIT:
                    return degree
            else:
                return degree

    def get_random_degrees(self, count: int, limit_octave=False) -> []:
        output = []

        for c in range(count):
            random_degree = self.get_random_degree(limit_octave=limit_octave)
            output.append(random_degree)

        return output
