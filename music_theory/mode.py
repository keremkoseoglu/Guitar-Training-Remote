import random
from music_theory.note import Note


class Mode:

    def __init__(self):
        self._modes = [
            # Major oriented
            "Ionian",
            "Dorian",
            "Phrygian",
            "Lydian",
            "Mixo",
            "Aeolian",
            "Locrian",

            # Melodic minor oriented
            "Jazz minor",
            "Dorian b2",
            "Lydian aug",
            "Lydian dom",
            "Mixo b6",
            "Half dim",
            "Altered"
        ]

    def get_mode_list(self) -> []:
        return self._modes

    def get_random_mode(self) -> str:
        random_note = Note().get_random_note()
        random_mode = self.get_random_mode_type()
        return random_note + " " + random_mode

    def get_random_mode_type(self) -> str:
        i = random.randint(0, len(self._modes) - 1)
        return self._modes[i]

    def get_random_modes(self, count: int, with_note=True) -> []:

        output = []
        note_obj = Note()

        for c in range(count):
            if with_note:
                random_note = note_obj.get_random_note() + " "
            else:
                random_note = ""
            random_mode = self.get_random_mode_type()
            random_result = random_note + random_mode
            output.append(random_result)

        return output
