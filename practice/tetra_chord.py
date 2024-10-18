""" Tetra chords """

from random import randint, sample
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from model.exercise import Exercise
from model.exercise_step import ExerciseStep
from music_theory.note import Note


class TetraChords(AbstractPractice):
    """Tetra chords"""

    _TITLE = "Tetra Chords"
    _SUBTITLE = "Play 4 note groupings on chords"

    _MAJOR_TETRA = ["1", "2", "3", "5"]
    _MINOR_TETRA = ["1", "b3", "4", "5"]
    _MINB5_TETRA = ["1", "b3", "4", "b5"]
    _DOM7B9_TETRA = ["1", "b2", "3", "5"]
    _ALL_TETRAS = [_MAJOR_TETRA, _MINOR_TETRA, _MINB5_TETRA, _DOM7B9_TETRA]

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """Returns random chord exercises"""
        if guitar["kind"] != "instrument":
            return None

        random_steps = []
        note = Note()

        for pos in range(0, quantity):  # pylint: disable=W0612
            rnd_notes = note.get_random_notes(randint(1, 4))

            rnd_note_txt = ""

            for rnd_note in rnd_notes:
                if rnd_note_txt != "":
                    rnd_note_txt += " | "
                rnd_note_txt += rnd_note

            rnd_group_txt = self._build_rnd_group_txt()

            step = ExerciseStep(rnd_note_txt, rnd_group_txt)
            random_steps.append(step)

        output = Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output

    def _build_rnd_group_txt(self) -> str:
        """Random group txt"""
        output = ""
        tetra_set = self._ALL_TETRAS[randint(0, len(self._ALL_TETRAS) - 1)]

        for pos in range(0, randint(1, 2)):
            if output != "":
                output += " | "

            random_sequence = sample([0, 1, 2, 3], 4)

            for pos in random_sequence:
                if output != "":
                    output += " "
                output += tetra_set[pos]

        return output
