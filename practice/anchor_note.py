""" Anchor note """
import random
from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from music_theory import chord, mode, note, scale
from performance.advice import Advice


class AnchorNote(AbstractPractice):
    """ Anchor note """
    _TITLE = "Anchor Note"
    _SUBTITLE = "Anchor note & use over..."

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns anchor note exercise """
        if guitar["kind"] != "instrument":
            return None

        advice = Advice()
        random_steps = []
        i = random.randint(0, 1)

        if i == 0:
            sub_txt = advice.get_random_advice()
            random_steps.append(exercise_step.ExerciseStep("random song", sub_txt))
        else:
            for random_note in note.Note().get_random_notes(count=quantity, same_shift=True):
                context_count = random.randint(1, 5)

                context_type = random.randint(0, 2)
                if context_type == 0:
                    stuff = chord.Chord().get_random_chords(context_count)
                elif context_type == 1:
                    stuff = mode.Mode().get_random_modes(context_count)
                else:
                    stuff = scale.Scale().get_random_scales(context_count)

                stuff_txt = ""
                for stuff_char in stuff:
                    if stuff_txt != "":
                        stuff_txt += " | "
                    stuff_txt += stuff_char

                random_step = exercise_step.ExerciseStep(random_note, stuff_txt)
                random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output
