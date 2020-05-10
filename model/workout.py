""" Workout module """
import random
from model.exercise import Exercise
from model.exercise_step import ExerciseStep
from model.guitar import Guitar


class WorkOut:
    """ Workout class """

    def __init__(self, exercises: []):
        self._exercises = exercises
        self._exercise_index = 0
        self._step_index = 0
        self.guitar = Guitar.UNDEFINED

    def add_guitar(self, guitar: Guitar):
        """ Adds a new instrument """
        guitar_step = ExerciseStep(guitar.name)
        guitar_exercise = Exercise("Guitar", "Pick the following guitar", [guitar_step])
        self._exercises.insert(0, guitar_exercise)

    def get_current_exercise(self) -> Exercise:
        """ Returns current exercise """
        try:
            return self._exercises[self._exercise_index]
        except Exception: # pylint: disable=W0703
            return None

    def get_current_step(self) -> ExerciseStep:
        """ Returns current step """
        current_exercise = self.get_current_exercise()
        if current_exercise is None:
            return None
        if len(current_exercise.steps) <= self._step_index:
            return None
        return current_exercise.steps[self._step_index]

    def get_next_step(self):
        """ Returns next step """
        current_exercise = self.get_current_exercise()
        if current_exercise is None:
            return None, None

        self._step_index += 1

        if self._step_index >= len(current_exercise.steps):
            self._step_index = 0
            self._exercise_index += 1

            if self._exercise_index >= len(self._exercises):
                return None, None
        return self.get_current_exercise(), self.get_current_step()

    def get_exercise_count(self) -> int:
        """ Returns exercise count """
        return len(self._exercises)

    def get_exercise_index(self) -> int:
        """ Returns exercise index """
        return self._exercise_index

    def get_step_count(self) -> int:
        """ Returns step count """
        return len(self.get_current_exercise().steps)

    def get_step_index(self) -> int:
        """ Returns step index """
        return self._step_index

    def remove_random_exercies(self, percentage: int):
        """ Removes random exercises from the dataset """
        target_count = int(len(self._exercises) * percentage / 100)

        while len(self._exercises) > target_count:
            abandon_index = random.randint(0, len(self._exercises) - 1)
            self._exercises.pop(abandon_index)

    def rewind(self):
        """ Rewind """
        self._exercise_index = 0
        self._step_index = 0
