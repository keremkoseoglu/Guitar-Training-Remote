from model import exercise, exercise_step
from music_theory import chord, degree
from practice import abstract_practice


class DegreeMemo(abstract_practice.AbstractPractice):

    _TITLE = "Degree memo"
    _SUBTITLE = "Tell the following note"

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        random_steps = []

        random_chords = chord.Chord().get_random_chords(quantity)
        random_degrees = degree.Degree().get_random_degrees(quantity)

        for i in range(quantity):
            random_step = exercise_step.ExerciseStep(random_chords[i] + " deg " + str(random_degrees[i]), "follow by playing on fretboard")
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
