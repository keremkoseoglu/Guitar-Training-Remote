""" Guitar module """
import random
from config import get_configuration


def get_random_guitar() -> dict:
    """ Returns a random guitar """
    config = get_configuration()
    random_number = random.randint(1, 100)

    for guitar in config["instruments"]:
        if guitar["from"] <= random_number and guitar["to"] >= random_number:
            return guitar

    raise Exception("Couldn't select an instrument")
