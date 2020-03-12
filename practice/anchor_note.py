from model import exercise, exercise_step
from practice import abstract_practice
from music_theory import chord, mode, note, scale
import random


class AnchorNote(abstract_practice.AbstractPractice):

    _TITLE = "Anchor Note"
    _SUBTITLE = "Anchor note & use over..."

    def get_exercise(self, quantity: int) -> exercise.Exercise:
        random_steps = []
        i = random.randint(0, 1)

        if i == 0:
            random_steps.append(exercise_step.ExerciseStep("random song"))
        else:
            for random_note in note.Note().get_random_notes(quantity):
                context_count = random.randint(1, 5)

                context_type = random.randint(0, 2)
                if context_type == 0:
                    stuff = chord.Chord().get_random_chords(context_count)
                elif context_type == 1:
                    stuff = mode.Mode().get_random_modes(context_count)
                else:
                    stuff = scale.Scale().get_random_scales(context_count)

                stuff_txt = ""
                for s in stuff:
                    if stuff_txt != "":
                        stuff_txt += " | "
                    stuff_txt += s

                random_step = exercise_step.ExerciseStep(random_note, stuff_txt)
                random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
