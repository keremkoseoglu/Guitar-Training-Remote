""" Triad pair arpeggios """

import random
from model import exercise, exercise_step
from music_theory.chord import Chord
from music_theory.degree import Degree
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory


class TriadPairArpeggio(AbstractPractice):
    """Triad pair arpeggios"""

    _TITLE = "Triad pair arpeggios"
    _SUBTITLE = "Play arpeggios on triad pairs"

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """Returns exercise"""
        if guitar["kind"] != "instrument":
            return None

        chord = Chord()
        degree = Degree()
        random_steps = []

        for _ in range(0, quantity):  # pylint: disable=W0612
            rnd_chords = chord.get_two_subsequent_whole_step_basic_chords()

            rnd_chord_txt = ""
            for rnd_chord in rnd_chords:
                if rnd_chord_txt != "":
                    rnd_chord_txt += " | "
                rnd_chord_txt += rnd_chord

            rnd_degrees = degree.get_random_chord_tones(random.randint(2, 4))
            rnd_degree_txt = ""

            for rnd_degree in rnd_degrees:
                if rnd_degree_txt != "":
                    rnd_degree_txt += " "
                rnd_degree_txt += str(rnd_degree)

            random_step = exercise_step.ExerciseStep(
                main_text=rnd_chord_txt, sub_text=rnd_degree_txt
            )
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output
