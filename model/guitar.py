""" Guitar module """
import random
from config import get_configuration, get_storage, save_storage


def get_random_guitar() -> dict:
    """ Returns a random guitar """
    config = get_configuration()
    storage = get_storage()

    while True:
        random_number = random.randint(1, 100)
        for guitar in config["instruments"]:
            if guitar["from"] <= random_number and guitar["to"] >= random_number:
                if guitar["type"] != storage["last_instrument"]:
                    storage["last_instrument"] = guitar["type"]
                    save_storage(storage)
                    return guitar

    raise Exception("Couldn't select an instrument")
