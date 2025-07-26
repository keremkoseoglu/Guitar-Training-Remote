""" Speed up module """
import random
from enum import Enum
from model.exercise import Exercise
from model.exercise_helper import get_external_metronome_helper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.arpeggio import Arpeggio
from practice.chord_connection import ChordConnection
from practice.idea_on_chords import IdeaOnChords
from practice.interval import Intervals
from practice.left_permutation import LeftFingerPermutations
from practice.scale_dexterity import ScaleDexterity
from practice.scale_on_chord import ScaleOnChord
from practice.transcribe_rep_org import TranscribeRepertoirAsOriginal
from practice.metronome import Metronome

class CoreSpeedUpPractice(Enum):
    """ Core speed up practice """
    ARPEGGIO = 1
    CHORD_CONNECTION = 2
    IDEA_ON_CHORDS = 3
    INTERVAL = 4
    LEFT_PERMUTATION = 5
    SCALE_DEXTERITY = 6
    SCALE_ON_CHORD = 7
    KNOWN_RIFF = 8

class SpeedUp(AbstractPractice):
    """ Speed up class """
    _TITLE = "Speed Up"
    _SUBTITLE = "Speed up with metronome"

    def __init__(self):
        self._metronome = Metronome()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.SPEED

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns random one liner exercises """
        if not (guitar["kind"] == "instrument" and guitar["strings"] > 0):
            return None

        core_exercise = SpeedUp._get_random_core_exercise(quantity, guitar)
        core_exercise.title = SpeedUp._TITLE
        core_exercise.description += f"\n{ SpeedUp._SUBTITLE }"

        for step in core_exercise.steps:
            random_bpm = self._metronome.get_random_bpm()
            metro_helper = get_external_metronome_helper(random_bpm)
            step.helpers.append(metro_helper)

        return core_exercise

    @staticmethod
    def _get_random_core_exercise(quantity: int, guitar: dict) -> Exercise: # pylint: disable=R0911
        """ Returns random core exercise """
        random_index = random.randint(0, len(CoreSpeedUpPractice) - 1)
        random_practice = CoreSpeedUpPractice(random_index)

        if random_practice == CoreSpeedUpPractice.ARPEGGIO:
            return Arpeggio().get_exercise(quantity, guitar)
        if random_practice == CoreSpeedUpPractice.CHORD_CONNECTION:
            return ChordConnection().get_exercise(quantity, guitar)
        if random_practice == CoreSpeedUpPractice.IDEA_ON_CHORDS:
            return IdeaOnChords().get_exercise(quantity, guitar)
        if random_practice == CoreSpeedUpPractice.INTERVAL:
            return Intervals().get_exercise(quantity, guitar)
        if random_practice == CoreSpeedUpPractice.KNOWN_RIFF:
            return TranscribeRepertoirAsOriginal().get_exercise(quantity, guitar)
        if random_practice == CoreSpeedUpPractice.LEFT_PERMUTATION:
            return LeftFingerPermutations().get_exercise(quantity, guitar)
        if random_practice == CoreSpeedUpPractice.SCALE_DEXTERITY:
            return ScaleDexterity().get_exercise(quantity, guitar)
        if random_practice == CoreSpeedUpPractice.SCALE_ON_CHORD:
            return ScaleOnChord().get_exercise(quantity, guitar)
        assert False
