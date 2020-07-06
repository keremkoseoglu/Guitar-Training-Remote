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

def get_storage() -> dict:
    """ Returns storage """
    output = {}
    file_path = _get_storage_path()
    with open(file_path) as storage_file:
        output = json.load(storage_file)
    return output

def save_storage(storage: dict):
    """ Writes storage to disk """
    file_path = _get_storage_path()
    with open(file_path, "w") as storage_file:
        json.dump(storage, storage_file)

def _get_config_path() -> str:
    return _get_path("config.json")

def _get_storage_path() -> str:
    return _get_path("storage.json")

def _get_path(file_name: str) -> str:
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)
    return file_path
