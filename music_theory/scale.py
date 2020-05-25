""" Scale module """
import random
from music_theory.note import Note
from music_theory.mode import Mode


class Scale:
    """ Scale """

    def __init__(self):
        self._scales = Mode().get_mode_list().copy()
        self._scales.append("Ionian Bebop")
        self._scales.append("Dorian Bebop")
        self._scales.append("Mixo Bebop")
        self._scales.append("Dim WH")
        self._scales.append("Dim HW")

    def get_random_scale(self) -> str:
        """ Returns a random scale """
        random_note = Note().get_random_note()
        random_scale = self.get_random_scale_type()
        return random_note + " " + random_scale

    def get_random_scale_type(self) -> str:
        """ Returns a random scale type """
        i = random.randint(0, len(self._scales) - 1)
        return self._scales[i]

    def get_random_scales(self, count: int, with_note=True) -> []:
        """ Returns random scales """

        output = []
        note_obj = Note()

        for count_pos in range(count): # pylint: disable=W0612
            if with_note:
                random_note = note_obj.get_random_note() + " "
            else:
                random_note = ""
            random_scale = self.get_random_scale_type()
            random_result = random_note + random_scale
            output.append(random_result)

        return output
