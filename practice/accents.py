""" Accent practices """
import random
from copy import copy
from enum import Enum
from model import exercise
from practice import abstract_practice
from practice.interval import Intervals
from practice.lazy_fingers import LazyFingers
from practice.notes_on_fretboard import NotesOnFretboard
from practice.notes_on_strings import NotesOnStrings
from practice.scale_degree_sequence import ScaleDegreeSequence
from practice.scale_dexterity import ScaleDexterity
from practice.arpeggio import Arpeggio
from config import get_configuration


class SupportPractice(Enum):
    """ Support practices """
    INTERVALS = 1
    LAZY_FINGERS = 2
    NOTES_ON_FRETBOARD = 3
    NOTES_ON_STRINGS = 4
    SCALE_DEGREE_SEQUENCE = 5
    SCALE_DEXTERITY = 6
    ARPEGGIO = 7


class Accents(abstract_practice.AbstractPractice):
    """ Accent practices """

    _TITLE = "Accents"

    def __init__(self):
        self._config = get_configuration()
        self._accents = []
        self._build_accents()

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns accent exercise """
        if guitar["strings"] <= 0:
            return None

        practice = Accents._get_support_practice()
        if practice is None:
            return None

        output = practice.get_exercise(quantity, guitar)
        accent = self._get_random_accent()
        output.title = "Accents"
        output.description += "\r\n with accent on: " + accent
        return output

    def _get_random_accent(self) -> str:
        output = []
        local_accents = copy(self._accents)
        random_accent_count = random.randint(1, len(local_accents)-1)
        while len(output) < random_accent_count:
            random_accent_pos = random.randint(0, len(local_accents)-1)
            random_accent = local_accents.pop(random_accent_pos)
            output.append(random_accent)
        output.sort()
        output_str = ""
        for accent in output:
            if output_str != "":
                output_str += " "
            output_str += accent
        return output_str

    def _build_accents(self):
        self._accents = []
        current_accent = 0
        while len(self._accents) < self._config["max_accent_notes"]:
            current_accent += 1
            self._accents.append(str(current_accent))

    @staticmethod
    def _get_support_practice() -> abstract_practice.AbstractPractice:
        support_index = random.randint(0, len(SupportPractice)-1)
        output = None
        for practice in SupportPractice:
            if practice.value == support_index:
                if practice == SupportPractice.ARPEGGIO:
                    output = Arpeggio()
                    break
                if practice == SupportPractice.INTERVALS:
                    output = Intervals()
                    break
                if practice == SupportPractice.LAZY_FINGERS:
                    output = LazyFingers()
                    break
                if practice == SupportPractice.NOTES_ON_FRETBOARD:
                    output = NotesOnFretboard()
                    break
                if practice == SupportPractice.NOTES_ON_STRINGS:
                    output = NotesOnStrings()
                    break
                if practice == SupportPractice.SCALE_DEGREE_SEQUENCE:
                    output = ScaleDegreeSequence()
                    break
                if practice == SupportPractice.SCALE_DEXTERITY:
                    output = ScaleDexterity()
                    break
        return output