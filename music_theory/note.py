""" Note module """
import random
from copy import deepcopy
from config import get_configuration

class Note:
    """ Note class """
    def __init__(self):
        self._config = get_configuration()

    def get_random_note(self) -> str:
        """ Returns a random note """
        i = random.randint(0, len(self._config["notes"]) - 1)
        return self._config["notes"][i]

    def get_random_notes(self, count) -> []:
        """ Returns random notes """
        output = []

        notes = deepcopy(self._config["notes"])
        for count_pos in range(count): # pylint: disable=W0612
            if len(notes) <= 0:
                break
            i = random.randint(0, len(notes) - 1)
            output.append(notes.pop(i))

        return output
