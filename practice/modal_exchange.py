""" Modal exchange chords """
import random
from typing import List
from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from config import get_configuration
from music_theory.mode import Mode


class ModalExchangeChords(AbstractPractice):
    """Modal exchange chords"""

    _TITLE = "Modal exchange"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.THEORY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """Returns modal exchange exercises"""
        random_steps = []

        for _ in range(0, quantity):
            chord_seq = self._build_random_chord_seq_str()
            random_step = exercise_step.ExerciseStep(chord_seq, "")
            random_steps.append(random_step)

        mode = Mode()
        subtitle = f"Root: {mode.get_random_mode_chord()}, exchange: {str(random.randint(2, 7))}"

        output = exercise.Exercise(
            self._TITLE,
            subtitle,
            random_steps,
            practice_category=self.category,
        )

        return output

    def _build_random_chord_seq(self) -> List[str]:
        chord_seq = []
        chord_count = random.randint(2, 4)
        had_exchange = False
        for chord_pos in range(0, chord_count):
            random_chord = str(random.randint(1, 7))
            if (chord_pos > 0 and random.randint(0, 1) == 1) or (
                chord_pos == chord_count - 1 and not had_exchange
            ):
                random_chord += "!"
                had_exchange = True
            chord_seq.append(random_chord)
        return chord_seq

    def _build_random_chord_seq_str(self) -> str:
        result = ""
        chord_seq = self._build_random_chord_seq()
        for chord in chord_seq:
            if result != "":
                result += " | "
            result += chord
        return result
