""" Configuration module """
import os
import json


_CONFIGURATION = {}


def get_configuration() -> dict:
    """ Returns configuration """
    global _CONFIGURATION
    if _CONFIGURATION == {}:
        file_path = _get_config_path()
        with open(file_path) as config_file:
            _CONFIGURATION = json.load(config_file)
    return  _CONFIGURATION

def edit_configuration():
    """ Edits the configuration file """
    file_path = _get_config_path()
    os.system("open " + file_path)

def _get_config_path() -> str:
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "config.json")
    return file_path
