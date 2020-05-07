""" Guitar module """
from enum import Enum
import random


class Guitar(Enum):
    """ Guitar types """
    UNDEFINED = 0
    BASS = 1
    ELECTRIC = 2
    ACOUSTIC = 3
    KEYS = 4


_GUITARS = [
    {"type": Guitar.BASS, "from": 1, "to": 50},
    {"type": Guitar.ELECTRIC, "from": 51, "to": 70},
    {"type": Guitar.ACOUSTIC, "from": 71, "to": 90},
    {"type": Guitar.KEYS, "from": 91, "to": 100},
]

def get_random_guitar() -> Guitar:
    """ Returns a random guitar """
    random_number = random.randint(1, 100)

    output = Guitar.UNDEFINED
    for guitar in _GUITARS:
        if guitar["from"] <= random_number and guitar["to"] >= random_number:
            output = guitar["type"]
            break

    return output
