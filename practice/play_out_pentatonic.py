""" Play out pentatonic """
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from model.exercise import Exercise
from model.exercise_step import ExerciseStep
from music_theory.note import Note
from music_theory.chord import Chord

class PlayOutPentatonic(AbstractPractice):
    """ Play out pentatonic """
    _TITLE = "Play out pentatonic"
    _SUBTITLE = "Play X pentatonic and target Y"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> Exercise:
        """ Returns random chord exercises """
        if guitar["kind"] != "instrument":
            return None

        random_steps = []
        note = Note()
        chord = Chord()

        for pos in range(0, quantity): # pylint: disable=W0612
            pentatonic_key = note.get_random_note()
            target_chord = chord.get_random_chord()
            step = ExerciseStep(
                f"{pentatonic_key} Pentatonic",
                target_chord)
            random_steps.append(step)

        output = Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output
