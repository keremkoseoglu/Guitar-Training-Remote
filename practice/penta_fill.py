"""Pentatonic fill"""

import random
from model import exercise, exercise_step
from music_theory import note
from music_theory.position import Position
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory


class PentaFill(AbstractPractice):
    """Pentatonic fill"""

    _TITLE = "Pentatonic Fill"
    _SUBTITLE = "Run pentatonic fills"

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """Returns pentatonic fill exercise"""
        if guitar["kind"] != "instrument":
            return None

        random_steps = []

        for _ in range(quantity):
            suggested_position = Position.get_random_chord_position()
            random_note = note.Note().get_random_note()
            penta = "maj" if random.randint(0, 1) == 0 else "min"

            random_step = exercise_step.ExerciseStep(
                f"{random_note} {penta}",
                f"Suggested position: {str(suggested_position)}",
            )

            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output
