""" Exercise helper module """
from enum import Enum
from config import get_configuration

class ExerciseHelperType(Enum):
    """ Defines an exercise helper type
    Examples: open browser, start metronome, etc """
    BROWSER = 1
    METRONOME = 2
    OS_COMMAND = 3
    BUTTONS = 4


class ExerciseHelper:
    """ Defines an exercise helper """
    def __init__(self, helper_type: ExerciseHelperType, params: {}=None):
        self.helper_type = helper_type
        if params is None:
            self.params = {}
        else:
            self.params = params


def get_flukebox_helper(playlist: str, no_local: bool = False) -> ExerciseHelper:
    """ Returns a FlukeBox helper Exercise """
    config = get_configuration()
    if "flukebox" not in config:
        return None
    command = "cd " + config["flukebox"]["path"] + ";"
    command += " venv/bin/python3 main.py playlist="
    command += config["flukebox"][playlist]
    if no_local:
        command += " no_local"
    output = ExerciseHelper(
        ExerciseHelperType.OS_COMMAND,
        {"command": command})
    return output
