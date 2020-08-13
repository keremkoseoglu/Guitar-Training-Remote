""" Degree memo """
from model import exercise, exercise_step
from music_theory import chord, degree
from practice import abstract_practice
from practice.practice_category import PracticeCategory


class DegreeMemo(abstract_practice.AbstractPractice):
    """ Degree memo """

    _TITLE = "Degree memo"
    _SUBTITLE = "Tell the following note"

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.THEORY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns degree memo exercises """
        random_steps = []
        random_chords = chord.Chord().get_random_chords(quantity)
        random_degrees = degree.Degree().get_random_degrees(quantity)

        for quantity_pos in range(quantity):
            random_step = exercise_step.ExerciseStep(
                random_chords[quantity_pos] + " deg " + str(random_degrees[quantity_pos]),
                "follow by playing")
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        return output
