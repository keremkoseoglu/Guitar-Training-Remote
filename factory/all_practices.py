""" All practices """
import random
from factory import abstract_factory
from model import workout
from model.guitar import Guitar
import practice.toolkit


class AllPractices(abstract_factory.AbstractFactory): # pylint: disable=R0903
    """ All practices """
    _MAX_STEPS_PER_EXERCISE = 5

    def get_workout(self, guitar: Guitar = Guitar.UNDEFINED) -> workout.WorkOut:
        """ Returns a new workout containing all practices """
        exercises = []
        practice_objects = practice.toolkit.Toolkit().get_all_practices()

        while len(practice_objects) > 0:
            random_practice_index = random.randint(0, len(practice_objects) - 1)
            practice_object = practice_objects[random_practice_index]

            random_step_count = random.randint(1, self._MAX_STEPS_PER_EXERCISE)
            produced_exercise = practice_object().get_exercise(random_step_count, guitar)
            if produced_exercise is not None:
                exercises.append(produced_exercise)
            practice_objects.pop(random_practice_index)

        output = workout.WorkOut(exercises)
        return output
