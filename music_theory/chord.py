import random
from music_theory.note import Note


class Chord:

    def __init__(self):
        self._chord_types = [
            "",
            "7",
            "∆7",
            "9",
            "#11",
            "sus4",
            "-",
            "-7",
            "-9",
            "-b9",
            "-11",
            "-13",
            "Ø",
            # Melodic minor oriented
            "-∆7",     # Jazz minor / melodic minor
            "b9sus4",  # Dorian b2 / Phrygian #6
            "∆7#5",    # Lydian aug / Lydian #5
            "7#11",    # Lydian dom / Lydian b7 / Overtone
            "7b13",    # Mixolydian b6 / Hindu
            "m7b5",    # Aeolian b5 / Locrian #2 / half dim
            "7alt"     # Altered / Super Logcian
        ]

    def get_random_chord_type(self) -> str:
        i = random.randint(0, len(self._chord_types) - 1)
        return self._chord_types[i]

    def get_random_chords(self, count: int) -> []:
        output = []
        note_obj = Note()

        for c in range(count):
            random_note = note_obj.get_random_note()
            random_chord_type = self.get_random_chord_type()
            random_result = random_note + random_chord_type
            output.append(random_result)

        return output
