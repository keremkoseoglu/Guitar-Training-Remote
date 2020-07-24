""" Double hand tap practices """
import random
from enum import Enum
from model import exercise
from practice import abstract_practice
from practice.arpeggio import Arpeggio
from practice.chord_connection import ChordConnection
from practice.chords import Chords
from practice.notes_on_fretboard import NotesOnFretboard
from practice.notes_on_strings import NotesOnStrings
from practice.scale_dexterity import ScaleDexterity
from practice.scale_on_chord import ScaleOnChord


class SupportPractice(Enum):
    """ Support practices """
    ARPEGGIO = 1
    CHORD_CONNECTION = 2
    CHORDS = 3
    NOTES_ON_FRETBOARD = 4
    NOTES_ON_STRINGS = 5
    SCALE_DEXTERITY = 6
    SCALE_ON_CHORD = 7


class DoubleHandTap(abstract_practice.AbstractPractice):
    """ Double hand tap exercise """
    _TITLE = "Double hand tap"

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns double hand tap exercise """
        if guitar["kind"] != "instrument":
            return None
        if guitar["strings"] <= 0:
            return None

        practice = DoubleHandTap._get_support_practice()
        if practice is None:
            return None

        output = practice.get_exercise(quantity, guitar)
        output.title = DoubleHandTap._TITLE
        output.description += "\r\n with double hand tap "
        return output

    @staticmethod
    def _get_support_practice() -> abstract_practice.AbstractPractice:
        support_index = random.randint(0, len(SupportPractice)-1)
        output = None
        for practice in SupportPractice:
            if practice.value == support_index:
                if practice == SupportPractice.ARPEGGIO:
                    output = Arpeggio()
                    break
                if practice == SupportPractice.CHORD_CONNECTION:
                    output = ChordConnection()
                    break
                if practice == SupportPractice.CHORDS:
                    output = Chords()
                    break
                if practice == SupportPractice.NOTES_ON_FRETBOARD:
                    output = NotesOnFretboard()
                    break
                if practice == SupportPractice.NOTES_ON_STRINGS:
                    output = NotesOnStrings()
                    break
                if practice == SupportPractice.SCALE_DEXTERITY:
                    output = ScaleDexterity()
                    break
                if practice == SupportPractice.SCALE_ON_CHORD:
                    output = ScaleOnChord()
                    break
        return output
