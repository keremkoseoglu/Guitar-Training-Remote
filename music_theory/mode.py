""" Mode module """
import random
from music_theory.note import Note
from config import get_configuration


class Mode:
    """Mode class"""

    def __init__(self):
        config = get_configuration()
        self._modes = []
        for mode in config["modes"]:
            self._modes.append(mode["mode"])

    def get_mode_list(self) -> []:
        """Returns a mode list"""
        return self._modes

    def get_random_mode(self) -> str:
        """Returns a random mode"""
        random_note = Note().get_random_note()
        random_mode = self.get_random_mode_type()
        return f"{random_note} {random_mode}"

    def get_random_mode_type(self) -> str:
        """Returns a random mode type"""
        i = random.randint(0, len(self._modes) - 1)
        return self._modes[i]

    def get_random_modes(self, count: int, with_note=True) -> []:
        """Returns random modes"""
        output = []
        note_obj = Note()

        for range_pos in range(count):  # pylint: disable=W0612
            if with_note:
                random_note = f"{note_obj.get_random_note()} "
            else:
                random_note = ""
            random_mode = self.get_random_mode_type()
            random_result = random_note + random_mode
            output.append(random_result)

        return output

    def get_random_mode_chord(self) -> str:
        """Returns a random mode chord"""
        random_note = Note().get_random_note()
        config = get_configuration()
        i = random.randint(0, len(config["modes"]) - 1)
        random_extension = config["modes"][i]["chord"]
        return f"{random_note}{random_extension}"
