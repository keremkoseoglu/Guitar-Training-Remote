"""Mind bending module
This module contains exercises for mind bending
"""

from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from music_theory.note import Note
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome


class MindBending(AbstractPractice):
    """Lazy fingers exercise class"""

    _TITLE = "Mind bending"
    _SUBTITLE = "Walk down the fretboard on:"

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.LEFT_HAND

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """Returns lazy fingers exercises"""
        if guitar["kind"] != "instrument":
            return None

        string_count = guitar["strings"]
        if string_count <= 0:
            return None

        metronome = Metronome()
        random_steps = []
        note = Note()

        for quantity_pos in range(quantity):  # pylint: disable=W0612
            random_note = note.get_random_note()
            random_bpm = metronome.get_random_bpm()

            random_step = exercise_step.ExerciseStep(random_note)

            random_step.helpers = [
                ExerciseHelper(ExerciseHelperType.METRONOME, {"bpm": random_bpm})
            ]

            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output
