""" Note module """

import random
from copy import deepcopy
from typing import List
from config import get_configuration


class Note:
    """Note class"""

    _SHARP = "#"
    _FLAT = "b"

    def __init__(self):
        self._config = get_configuration()

    def get_random_note(self) -> str:
        """Returns a random note"""
        i = random.randint(0, len(self._config["notes"]) - 1)
        return self._config["notes"][i]

    def get_random_notes(self, count, same_shift: bool = False) -> List:
        """Returns random notes"""
        output = []
        returnable_shift = ""
        notes = deepcopy(self._config["notes"])

        for count_pos in range(count):  # pylint: disable=W0612
            if len(notes) <= 0:
                break

            random_note = ""

            while random_note == "":
                i = random.randint(0, len(notes) - 1)
                random_note = notes[i]

                if same_shift:
                    if Note._FLAT in random_note:
                        note_shift = Note._FLAT
                    elif Note._SHARP in random_note:
                        note_shift = Note._SHARP
                    else:
                        note_shift = ""

                    if returnable_shift == "":
                        if note_shift != "":
                            returnable_shift = note_shift
                    else:
                        if note_shift != "" and note_shift != returnable_shift:
                            random_note = ""
                            continue

                notes.pop(i)

            output.append(random_note)

        return output

    def get_two_subsequent_whole_step_notes(self) -> List:
        """Returns two subsequent notes"""
        note1 = self.get_random_note()

        if "#" in note1:
            note2_candidates = self._config["sharpy_notes"]
        else:
            note2_candidates = self._config["flatty_notes"]

        note1_idx = note2_candidates.index(note1)
        note2_idx = note1_idx + 2

        if note2_idx > len(note2_candidates) - 1:
            note2_idx -= len(note2_candidates)

        note2 = note2_candidates[note2_idx]

        return [note1, note2]
