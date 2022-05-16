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
    EXTERNAL_METRONOME = 5


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

    command = f"cd {config['flukebox']['path']} ;" \
              f" venv/bin/python3 main.py playlist={config['flukebox'][playlist]}" \
              f"{' no_local' if no_local else ''}"

    output = ExerciseHelper(ExerciseHelperType.OS_COMMAND,
                            {"command": command})
    return output

def get_external_metronome_helper(bpm: int) -> ExerciseHelper:
    """ Returns a metronome helper Exercise """
    config = get_configuration()
    if "metronome_app" not in config:
        return None
    command = config["metronome_app"]["path"].replace(" ", "\ ") #pylint: disable=W1401
    command = "open " + command
    output = ExerciseHelper(ExerciseHelperType.OS_COMMAND,
                            {"command": command, "clipboard": str(bpm)})
    return output
