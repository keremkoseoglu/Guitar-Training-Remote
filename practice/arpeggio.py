""" Arpeggio """
import random
from model import exercise, exercise_step
from music_theory import chord, scale
from music_theory.position import Position
from practice import abstract_practice
from practice.practice_category import PracticeCategory
from config import get_configuration


class Arpeggio(abstract_practice.AbstractPractice):
    """ Arpeggio """

    _TITLE = "Arpeggio"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns arpeggio exercise """
        if guitar["kind"] != "instrument":
            return None

        # ---Preparation-----

        random_steps = []
        random_scales = []

        # ---Build random list-----

        random_chords = chord.Chord().get_random_chords(quantity)
        quantity_left = quantity - len(random_chords)
        if quantity_left > 0:
            random_scales = scale.Scale().get_random_scales(quantity_left)

        random_stuff = []

        for i in range(len(random_chords)):
            random_stuff.append(random_chords[i])

        try:
            for i in range(len(random_scales)):
                random_stuff.append(random_scales[i])
        except Exception:
            pass

        # ---Build return list-----

        for random_arp in random_stuff:
            suggested_position = Position.get_random_chord_position()

            random_step = exercise_step.ExerciseStep(
                random_arp,
                "Suggested position: " + str(suggested_position))

            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._get_arpeggio_type(),
            random_steps,
            practice_category=self.category)

        return output

    def _get_arpeggio_type(self) -> str:
        random_index = random.randint(0, len(self._config["arpeggios"]) - 1)
        return self._config["arpeggios"][random_index]
