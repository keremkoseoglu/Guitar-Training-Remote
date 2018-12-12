from factory import abstract_factory
from model import exercise, exercise_step, workout


class TestFactory(abstract_factory.AbstractFactory):

    def get_workout(self) -> workout.WorkOut:

        step_1_1 = exercise_step.ExerciseStep("Step 1.1", 2, "last 2 secs")
        step_1_2 = exercise_step.ExerciseStep("Step 1.2", 2, "last 2 secs")
        exercise_1 = exercise.Exercise("First exercise", "subinfo 1", [step_1_1, step_1_2])

        step_2_1 = exercise_step.ExerciseStep("Step 2.1", 2, "last 2 secs")
        step_2_2 = exercise_step.ExerciseStep("Step 2.2", 2, "last 2 secs")
        exercise_2 = exercise.Exercise("Second exercise", "subinfo 2", [step_2_1, step_2_2])

        output = workout.WorkOut([exercise_1, exercise_2])

        return output
