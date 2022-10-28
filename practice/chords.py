""" Chords """
import random
from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from music_theory import chord
from music_theory.position import Position


class Chords(AbstractPractice):
    """ Chords """
    _TITLE = "Chords"
    _SUBTITLES = ["Play the following chords",
                  "Play walking bass lines",
                  "Play with common notes"]
    _STEP_TXT = "From positions"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random chord exercises """
        if guitar["kind"] != "instrument":
            return None

        random_steps = []

        for chord_pos in range(0, quantity): # pylint: disable=W0612
            context_count = random.randint(2, 4)
            stuff = chord.Chord().get_random_chords(context_count)

            stuff_txt = ""
            for stuff_char in stuff:
                if stuff_txt != "":
                    stuff_txt += " | "
                stuff_txt += f"({Chords._get_random_position()})"
                stuff_txt += f" {stuff_char}"

            random_step = exercise_step.ExerciseStep(
                Chords._STEP_TXT,
                stuff_txt)

            random_steps.append(random_step)

        subtitle = Chords._SUBTITLES[random.randint(0, len(Chords._SUBTITLES) - 1)]

        output = exercise.Exercise(
            self._TITLE,
            subtitle,
            random_steps,
            practice_category=self.category)

        return output

    @staticmethod
    def _get_random_position():
        random_position = Position.get_random_chord_position()
        return f"P{random_position}"
