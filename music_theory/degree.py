""" Degree module """

import random
from typing import List
from config import get_configuration


class Degree:
    """Degree class"""

    _OCTAVE_LIMIT = 7

    def __init__(self):
        config = get_configuration()
        self._degrees = config["degrees"]

    def get_random_degree(
        self, limit_octave=False, exclude_unison=False, min_degree=0
    ) -> int:
        """Returns a random degree"""
        while True:
            i = random.randint(0, len(self._degrees) - 1)
            degree = self._degrees[i]
            if exclude_unison and degree in (1, 8):
                continue
            if limit_octave and degree > self._OCTAVE_LIMIT:
                continue
            if degree < min_degree:
                continue
            return degree

    def get_random_degrees(
        self, count: int, limit_octave=False, exclude_unison=False, min_degree=0
    ) -> List:
        """Returns random degrees"""
        output = []

        for range_pos in range(count):  # pylint: disable=W0612
            random_degree = self.get_random_degree(
                limit_octave=limit_octave,
                exclude_unison=exclude_unison,
                min_degree=min_degree,
            )
            output.append(random_degree)

        return output

    def get_random_chord_tones(self, count: int) -> List:
        """Returns random chord tones"""
        output = []
        chord_tones = [1, 3, 5, 7]
        for _ in range(count):
            random_idx = random.randint(0, len(chord_tones) - 1)
            chord_tone = chord_tones.pop(random_idx)
            output.append(chord_tone)
        return output
