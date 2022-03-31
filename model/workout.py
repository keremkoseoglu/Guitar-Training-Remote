""" Workout module """
import random
from typing import List
from model.exercise import Exercise
from model.exercise_step import ExerciseStep


class WorkOut:
    """ Workout class """

    def __init__(self, exercises: List):
        self._exercises = exercises
        self._exercise_index = 0
        self._step_index = 0
        self.guitar = {}

    @property
    def exercises(self) -> List:
        """ Exercises in workout """
        return self._exercises

    def add_guitar(self, guitar: dict):
        """ Adds a new instrument """
        guitar_step = ExerciseStep(guitar["type"])
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

        out_exercise = self.get_current_exercise()
        out_step = self.get_current_step()
        return out_exercise, out_step

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

    def remove_random_exercises(self,
                                remain: int,
                                preserve: List[str] = None):
        """ Removes random exercises from the dataset """
        if preserve is not None and len(preserve) > 0:
            for exercise_title in preserve:
                found = False
                for exercise in self._exercises:
                    if exercise_title == exercise.title:
                        found = True
                        break
                if not found:
                    #raise Exception("Invalid preservable exercise " + exercise_title)
                    return

        while len(self._exercises) > remain:
            abandon_index = random.randint(0, len(self._exercises) - 1)
            if preserve is not None:
                exercise = self._exercises[abandon_index]
                if exercise.title in preserve:
                    continue
            self._exercises.pop(abandon_index)

    def rewind(self):
        """ Rewind """
        self._exercise_index = 0
        self._step_index = 0
