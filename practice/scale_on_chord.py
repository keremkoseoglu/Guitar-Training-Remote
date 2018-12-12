from model import exercise, exercise_step
from music_theory import chord, position
from practice import abstract_practice


class ScaleOnChord(abstract_practice.AbstractPractice):

    _TITLE = "Scale on chord"
    _SUBTITLE = "Play a scale on top of chord"

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        random_steps = []

        random_chords = chord.Chord().get_random_chords(quantity)

        for random_chord in random_chords:
            random_step = exercise_step.ExerciseStep(random_chord, super(ScaleOnChord, self).get_random_position_suggestion_text())
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
