""" Common notes between chords """
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from music_theory.chord import Chord
from model.exercise import Exercise
from model.exercise_step import ExerciseStep

class CommonChordNotes(AbstractPractice):
    """ Common notes between chords """
    _TITLE = "Common chord notes"
    _SUBTITLE = "Find common notes of chords"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.THEORY

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns random chord exercises """
        random_steps = []
        chord = Chord()

        while len(random_steps) < quantity:
            chords = chord.get_random_chords(2)
            random_step = ExerciseStep(f"{chords[0]} | {chords[1]}", "Play transition")
            random_steps.append(random_step)

        output = Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output
