import random
from model.exercise import Exercise
from model.exercise_step import ExerciseStep
from model.guitar import Guitar


class WorkOut:

    def __init__(self, exercises: []):
        self._exercises = exercises
        self._exercise_index = 0
        self._step_index = 0
        self.guitar = Guitar.UNDEFINED

    def add_guitar(self, guitar: Guitar):
        guitar_step = ExerciseStep(guitar.name)
        guitar_exercise = Exercise("Guitar", "Pick the following guitar", [guitar_step])
        self._exercises.insert(0, guitar_exercise)

    def get_current_exercise(self) -> Exercise:
        try:
            return self._exercises[self._exercise_index]
        except:
            return None

    def get_current_step(self) -> ExerciseStep:
        return self.get_current_exercise().steps[self._step_index]

    def get_next_step(self):
        current_exercise = self.get_current_exercise()
        if current_exercise is None:
            return

        self._step_index += 1

        if self._step_index >= len(current_exercise.steps):
            self._step_index = 0
            self._exercise_index += 1

            if self._exercise_index >= len(self._exercises):
                return None, None
            else:
                return self.get_current_exercise(), self.get_current_step()
        else:
            return self.get_current_exercise(), self.get_current_step()

    def get_exercise_count(self) -> int:
        return len(self._exercises)

    def get_exercise_index(self) -> int:
        return self._exercise_index

    def get_step_count(self) -> int:
        return len(self.get_current_exercise().steps)

    def get_step_index(self) -> int:
        return self._step_index

    def remove_random_exercies(self, percentage: int):

        target_count = int(len(self._exercises) * percentage / 100)

        while len(self._exercises) > target_count:
            abandon_index = random.randint(0, len(self._exercises) - 1)
            self._exercises.pop(abandon_index)

    def rewind(self):
        self._exercise_index = 0
        self._step_index = 0
