""" Chord connection """
import random
from model import exercise, exercise_step
from practice import improv
from practice.practice_category import PracticeCategory
from music_theory import chord


class ChordConnection():
    """ Chord connection
    PROTOCOL: AbstractPractice
    """
    _TITLE = "Chord Connection"
    _SUBTITLE = "Connect chords via"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random chord connection exercises """
        if guitar["kind"] != "instrument":
            return None

        random_steps = []
        random_improvs = improv.Improv().get_improvs(quantity)

        for random_improv in random_improvs:
            context_count = random.randint(2, 4)
            stuff = chord.Chord().get_random_chords(context_count)

            stuff_txt = ""
            for stuff_char in stuff:
                if stuff_txt != "":
                    stuff_txt += " | "
                stuff_txt += stuff_char

            random_step = exercise_step.ExerciseStep(random_improv, stuff_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)
        return output
