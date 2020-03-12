import random


class Note:
    def __init__(self):
        self._notes = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]

    def get_random_note(self) -> str:
        i = random.randint(0, len(self._notes) - 1)
        return self._notes[i]

    def get_random_notes(self, count) -> []:
        output = []

        notes = self._notes
        for r in range(count):
            if len(notes) <= 0:
                break
            i = random.randint(0, len(notes) - 1)
            output.append(notes.pop(i))

        return output
