import random
from music_theory.note import Note
from music_theory.mode import Mode


class Scale:

    def __init__(self):
        self._scales = Mode().get_mode_list().copy()
        self._scales.append("Ionian Bebop")
        self._scales.append("Dorian Bebop")
        self._scales.append("Mixo Bebop")
        self._scales.append("Dim WH")
        self._scales.append("Dim HW")

    def get_random_scale(self) -> str:
        random_note = Note().get_random_note()
        random_scale = self.get_random_scale_type()
        return random_note + " " + random_scale

    def get_random_scale_type(self) -> str:
        i = random.randint(0, len(self._scales) - 1)
        return self._scales[i]

    def get_random_scales(self, count: int, with_note=True) -> []:

        output = []
        note_obj = Note()

        for c in range(count):
            if with_note:
                random_note = note_obj.get_random_note() + " "
            else:
                random_note = ""
            random_scale = self.get_random_scale_type()
            random_result = random_note + random_scale
            output.append(random_result)

        return output
