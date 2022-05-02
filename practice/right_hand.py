""" Right hand """
from enum import Enum
import random
from model import exercise
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome
from practice.accents import Accents
from practice.anchor_note import AnchorNote
from practice.arpeggio import Arpeggio
from practice.interval import Intervals
from practice.left_permutation import LeftFingerPermutations
from practice.notes_on_fretboard import NotesOnFretboard
from practice.notes_on_strings import NotesOnStrings
from practice.scale_degree_sequence import ScaleDegreeSequence
from practice.scale_dexterity import ScaleDexterity
from practice.scale_on_chord import ScaleOnChord
from practice.chord_connection import ChordConnection
from practice.chords import Chords
import technique.right_hand


class SupportPractice(Enum):
    """ Support practices """
    ACCENTS = 1
    ANCHOR_NOTE = 2
    ARPEGGIO = 3
    INTERVAL = 4
    LEFT_PERMUTATION = 5
    NOTES_ON_FRETBOARD = 6
    NOTES_ON_STRINGS = 7
    SCALE_DEGREE_SEQUENCE = 8
    SCALE_DEXTERITY = 9
    SCALE_ON_CHORD = 10
    CHORD_CONNECTION = 11
    CHORDS = 12

class RightHand():
    """ Right hand exercises
    PROTOCOL: AbstractPractice
    """
    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.RIGHT_HAND

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns double thumb exercises """
        techs = technique.right_hand.RightHand().get_random_techniques(1)
        if techs is None:
            return None
        tech = techs[0]

        practice = RightHand._get_support_practice()
        if practice is None:
            return None

        output = practice.get_exercise(quantity, guitar)
        if output is None:
            return None
        output.title = tech
        output.description += "\r\nwith " + tech
        output.practice_category = self.category

        metronome = Metronome()

        for step_pos in range(0, len(output.steps)):
            step = output.steps[step_pos]
            random_bpm = metronome.get_random_bpm()

            if step.helpers is None:
                step.helpers = []

            step.helpers.append(ExerciseHelper(ExerciseHelperType.METRONOME,
                                               {"bpm": random_bpm}))

        return output

    @staticmethod
    def _get_support_practice() -> AbstractPractice:
        support_index = random.randint(0, len(SupportPractice)-1)
        output = None
        for practice in SupportPractice:
            if practice.value == support_index:
                if practice == SupportPractice.ACCENTS:
                    output = Accents()
                    break
                if practice == SupportPractice.ANCHOR_NOTE:
                    output = AnchorNote()
                    break
                if practice == SupportPractice.ARPEGGIO:
                    output = Arpeggio()
                    break
                if practice == SupportPractice.INTERVAL:
                    output = Intervals()
                    break
                if practice == SupportPractice.LEFT_PERMUTATION:
                    output = LeftFingerPermutations()
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
                if practice == SupportPractice.SCALE_ON_CHORD:
                    output = ScaleOnChord()
                    break
                if practice == SupportPractice.CHORD_CONNECTION:
                    output = ChordConnection()
                    break
                if practice == SupportPractice.CHORDS:
                    output = Chords()
                    break
        return output
