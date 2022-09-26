""" Configuration module """
import os
import json


_CONFIGURATION = {}
_DATA_DIR = "data"


def get_configuration() -> dict:
    """ Returns configuration """
    global _CONFIGURATION
    if not _CONFIGURATION:
        file_path = _get_config_path()
        with open(file_path, encoding="utf-8") as config_file:
            _CONFIGURATION = json.load(config_file)
    return  _CONFIGURATION

def edit_configuration():
    """ Edits the configuration file """
    file_path = _get_config_path()
    os.system(f"open {file_path}")

def get_storage() -> dict:
    """ Returns storage """
    output = {}
    file_path = _get_storage_path()
    with open(file_path, encoding="utf-8") as storage_file:
        output = json.load(storage_file)
    return output

def save_configuration():
    """ Saves configuration to the disk """
    file_path = _get_config_path()
    with open(file_path, "w", encoding="utf-8") as config_file:
        json.dump(_CONFIGURATION, config_file)

def save_storage(storage: dict):
    """ Writes storage to disk """
    file_path = _get_storage_path()
    with open(file_path, "w", encoding="utf-8") as storage_file:
        json.dump(storage, storage_file, indent=4)

def get_file_path(file_name: str) -> str:
    """ Returns path for file """
    data_dir = get_data_dir_path()
    file_path = os.path.join(data_dir, file_name)
    return file_path

def get_dir_path(dir_name: str) -> str:
    """ Returns path for file """
    data_dir = get_data_dir_path()
    dir_path = os.path.join(data_dir, dir_name)
    return dir_path

def get_data_dir_path() -> str:
    """ Returns path for a dir """
    current_dir = os.getcwd()
    dir_path = os.path.join(current_dir, _DATA_DIR)
    return dir_path

def _get_config_path() -> str:
    return get_file_path("config.json")

def _get_storage_path() -> str:
    return get_file_path("storage.json")
