""" Right hand disco exercises """

from typing import List
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome
from music_theory.note import Note


class Disco(AbstractPractice):
    """Right hand disco exercises"""

    _TITLE = "Disco"
    _SUBTITLE = "Play using right hand disco pattern"

    @property
    def category(self):
        """Returns the category of the practice"""
        return PracticeCategory.RIGHT_HAND

    def get_exercise(self, quantity, guitar):
        """Returns disco exercises"""
        if guitar["kind"] != "instrument":
            return None

        note = Note()
        metronome = Metronome()
        random_steps = self._generate_random_steps(quantity, note, metronome)

        output = exercise.Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output

    def _generate_rnd_note_txt(self, note: Note) -> str:
        rnd_notes = note.get_random_notes(4, same_shift=True)
        rnd_note_txt = ""
        for rnd_note in rnd_notes:
            if rnd_note_txt != "":
                rnd_note_txt += " | "
            rnd_note_txt += rnd_note
        return rnd_note_txt

    def _generate_random_step(self, note, metronome) -> exercise_step.ExerciseStep:
        rnd_note_txt = self._generate_rnd_note_txt(note)

        random_bpm = metronome.get_random_bpm()

        random_step = exercise_step.ExerciseStep(rnd_note_txt)

        random_step.helpers = [
            ExerciseHelper(ExerciseHelperType.METRONOME, {"bpm": random_bpm})
        ]
        return random_step

    def _generate_random_steps(
        self, quantity, chord, metronome
    ) -> List[exercise_step.ExerciseStep]:
        random_steps = []

        for quantity_pos in range(quantity):  # pylint: disable=W0612
            random_step = self._generate_random_step(chord, metronome)
            random_steps.append(random_step)

        return random_steps
