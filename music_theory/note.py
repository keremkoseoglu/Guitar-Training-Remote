""" Note module """
import random


class Note:
    """ Note class """
    def __init__(self):
        self._notes = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"] # pylint: disable=C0301

    def get_random_note(self) -> str:
        """ Returns a random note """
        i = random.randint(0, len(self._notes) - 1)
        return self._notes[i]

    def get_random_notes(self, count) -> []:
        """ Returns random notes """
        output = []

        notes = self._notes
        for count_pos in range(count): # pylint: disable=W0612
            if len(notes) <= 0:
                break
            i = random.randint(0, len(notes) - 1)
            output.append(notes.pop(i))

        return output
