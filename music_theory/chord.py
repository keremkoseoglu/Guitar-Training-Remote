""" Chord module """
import random
from music_theory.key_signature import KeySignature
from config import get_configuration


class Chord:
    """ Chord class """

    def __init__(self):
        config = get_configuration()
        self._chord_types = config["chord_types"]
        self._key_signature = KeySignature()

    def get_random_chord_type(self) -> str:
        """ Retuns random chord types """
        i = random.randint(0, len(self._chord_types) - 1)
        return self._chord_types[i]

    def get_random_chords(self, count: int) -> []:
        """ Returns random chords """
        output = []

        for count_pos in range(count): # pylint: disable=W0612
            random_note = self._key_signature.get_random_note()
            random_chord_type = self.get_random_chord_type()
            random_result = random_note + random_chord_type
            output.append(random_result)

        return output

    def get_random_chord(self) -> []:
        """ Returns a random chord """
        return self.get_random_chords(1)[0]
