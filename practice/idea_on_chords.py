""" Any idea can be used with any chord """
import random
from model import exercise, exercise_step
from practice.practice_category import PracticeCategory
from music_theory.chord import Chord

class IdeaOnChords():
    """ Any idea can be used with any chord
    PROTOCOL: AbstractPractice
    """

    _TITLE = "Idea on chord"
    _SUBTITLE = "Play the same idea over chords"
    _MAX_CHORDS = 4

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.DEXTERITY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random chord exercises """
        if guitar["kind"] != "instrument":
            return None

        random_steps = []
        chord = Chord()

        while len(random_steps) < quantity:
            random_chord_count = random.randint(2, 5)
            random_chords = []
            while len(random_chords) < random_chord_count:
                random_chord = chord.get_random_chord()
                random_chords.append(random_chord)

            random_chord_txt = ""
            for random_chord in random_chords:
                if random_chord_txt != "":
                    random_chord_txt += "  |  "
                random_chord_txt += random_chord

            random_step = exercise_step.ExerciseStep(
                "Random Idea",
                random_chord_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output
