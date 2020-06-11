""" Configuration module """
import os
import json


_CONFIGURATION = {}


def get_configuration() -> dict:
    """ Returns configuration """
    global _CONFIGURATION
    if _CONFIGURATION == {}:
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, "config.json")
        with open(file_path) as config_file:
            _CONFIGURATION = json.load(config_file)
    return  _CONFIGURATION
