""" Metronome quintuplets """
import random
from model.exercise import Exercise
from practice.practice_category import PracticeCategory
from practice.metronome import Metronome


class MetronomeQuintuplet:
    """Metronome quintuplet class"""

    def __init__(self):
        self._metronome = Metronome()

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return self._metronome.category

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """Returns metronome exercises"""
        output = self._metronome.get_exercise(quantity, guitar)
        output.title = " Quintuplet"
        output.description += (
            f" in {MetronomeQuintuplet._get_random_quintuplet_string()}"
        )
        return output

    @staticmethod
    def _get_random_quintuplet_string() -> str:
        chars = ["o", "o", "o", "o", "o"]
        result_positions = [1, 2, 3, 4, 5]
        x_count = random.randint(1, 5)
        x_pos = 0
        while x_pos < x_count:
            x_pos += 1
            result_pos = result_positions.pop(
                random.randint(0, len(result_positions) - 1)
            )
            chars[result_pos] = "X"
        result = "".join(chars)
        return result
