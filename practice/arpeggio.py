from model import exercise, exercise_step
from music_theory import chord, position, scale
from practice import abstract_practice
import random

class Arpeggio(abstract_practice.AbstractPractice):

    _TITLE = "Arpeggio"

    _ARPEGGIO_TYPES = [
        "Do an arpeggio on the given scale",
        "Walk diatonic arpeggios from scale"
    ]

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        # ---Preparation-----

        random_steps = []
        position_obj = position.Position()

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
        except:
            pass

        # ---Build return list-----

        for random_arp in random_stuff:
            suggested_position = position_obj.get_random_position()

            random_step = exercise_step.ExerciseStep(random_arp, "Suggested position: " + str(suggested_position))
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._get_arpeggio_type(), random_steps)
        return output

    def _get_arpeggio_type(self) -> str:
        random_index = random.randint(0, len(self._ARPEGGIO_TYPES) - 1)
        return self._ARPEGGIO_TYPES[random_index]