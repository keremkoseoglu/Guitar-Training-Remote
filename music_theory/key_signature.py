""" Key signature module """
import random
from config import get_configuration

class KeySignature:
    """ Key signature class """
    _MAX_ODDITIES = 7
    _CHORD_TYPES = ["major", "minor"]
    _ODDITIES = ["sharps", "flats"]

    def __init__(self):
        config = get_configuration()
        self._url = config["key_signature_url"]
        self._signatures = config["key_signatures"]

    @property
    def url(self) -> str:
        """ Answer URL """
        return self._url

    def get_random_chord_type(self) -> str:
        """ Returns random chord type """
        type_index = random.randint(0, 1)
        return self._CHORD_TYPES[type_index]

    def get_random_note(self) -> str:
        """ Returns a random note """
        key_sig_idx = random.randint(0, len(self._signatures) - 1)
        key_sig = self._signatures[key_sig_idx]
        chord_type = self.get_random_chord_type()
        note = key_sig[chord_type]
        return note

    def get_random_relative_note(self, relative: str) -> str:
        """ Returns a random relative note """
        while True:
            random_note = self.get_random_note()
            if not ("b" in random_note or "#" in random_note):
                return random_note
            if "b" in relative:
                if "b" in random_note:
                    return random_note
            elif "#" in relative:
                if "#" in random_note:
                    return random_note
            else:
                return random_note

    def get_random_chord_and_key_sig(self) -> tuple:
        """ Returns random chord and key signature """
        key_sig_idx = random.randint(0, len(self._signatures) - 1)
        key_sig = self._signatures[key_sig_idx]
        chord_type = self.get_random_chord_type()
        chord = key_sig[chord_type]
        if chord_type == "minor":
            chord += "m"
        return chord, key_sig

    def get_random_chord(self) -> str:
        """ Returns random chord """
        chord, key_sig = self.get_random_chord_and_key_sig() # pylint: disable=W0612
        return chord

    def get_random_chord_and_oddity(self) -> tuple:
        """ Returns random chord and oddity """
        chord, key_sig = self.get_random_chord_and_key_sig()

        for oddity_candidate in self._ODDITIES:
            if len(key_sig[oddity_candidate]) > 0:
                oddity = oddity_candidate
                break

        return chord, oddity

    def get_random_oddity(self) -> str:
        """ Returns random oddity """
        odd_index = random.randint(0, 1)
        return self._ODDITIES[odd_index]

    def get_random_oddity_count(self) -> int:
        """ Returns random oddity count """
        return random.randint(0, self._MAX_ODDITIES)

    def get_random_odd_node(self) -> str:
        """ Returns random odd note """
        odds = []
        while len(odds) <= 0:
            key_sig_idx = random.randint(0, len(self._signatures) - 1)
            key_sig = self._signatures[key_sig_idx]
            oddity = self.get_random_oddity()
            odds = key_sig[oddity]

        odd_index = random.randint(0, len(odds)-1)
        odd = odds[odd_index]
        return odd
