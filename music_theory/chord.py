""" Chord module """
import random
from music_theory.note import Note
from config import get_configuration


class Chord:
    """ Chord class """

    def __init__(self):
        config = get_configuration()
        self._chord_types = config["chord_types"]

    def get_random_chord_type(self) -> str:
        """ Retuns random chord types """
        i = random.randint(0, len(self._chord_types) - 1)
        return self._chord_types[i]

    def get_random_chords(self, count: int) -> []:
        """ Returns random chords """
        output = []
        note_obj = Note()

        for count_pos in range(count): # pylint: disable=W0612
            random_note = note_obj.get_random_note()
            random_chord_type = self.get_random_chord_type()
            random_result = random_note + random_chord_type
            output.append(random_result)

        return output

    def get_random_chord(self) -> []:
        """ Returns a random chord """
        return self.get_random_chords(1)[0]
