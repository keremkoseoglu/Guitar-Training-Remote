""" All practices """
import random
from vibhaga.inspector import Inspector, Container
from factory import abstract_factory
from model import workout
from config import get_configuration


class AllPractices(abstract_factory.AbstractFactory): # pylint: disable=R0903
    """ All practices """

    def __init__(self):
        self._config = get_configuration()

    def get_workout(self, guitar: dict = None) -> workout.WorkOut:
        """ Returns a new workout containing all practices """
        exercises = []
        practice_objects = Inspector.get_classes_in_container(
            Container(["practice"]),
            ["abstract"],
            [
                "AbstractPractice",
                "AbstractUrlList",
                "PracticeCategory",
                "PracticeCategoryGroup",
                "Position",
                "Guitar",
                "SupportPractice",
                "Accent"
            ])

        AllPractices._delete_duplicates(practice_objects)

        if "only_select" in self._config["practice_selection"]:
            only_select = self._config["practice_selection"]["only_select"]
            if only_select != "":
                for practice_object in practice_objects:
                    if practice_object.__module__ == only_select:
                        random_step_count = self._get_random_step_count()
                        produced_exercise = practice_object().get_exercise(
                            random_step_count,
                            guitar)
                        exercises.append(produced_exercise)
                        output = workout.WorkOut(exercises)
                        return output

        while len(practice_objects) > 0:
            random_practice_index = random.randint(0, len(practice_objects) - 1)
            practice_object = practice_objects[random_practice_index]

            random_step_count = self._get_random_step_count()
            produced_exercise = practice_object().get_exercise(random_step_count, guitar)
            if produced_exercise is not None:
                exercises.append(produced_exercise)
            practice_objects.pop(random_practice_index)

        output = workout.WorkOut(exercises)
        return output

    def _get_random_step_count(self):
        return random.randint(
            1,
            self._config["practice_selection"]["max_steps_per_exercise"])

    @staticmethod
    def _delete_duplicates(practice_objects):
        module_count = {}

        for practice_object in practice_objects:
            if practice_object.__module__ not in module_count:
                module_count[practice_object.__module__] = 0
            module_count[practice_object.__module__] += 1

        for module in module_count:
            if module_count[module] <= 1:
                continue
            practice_index = -1
            practice_cursor = -1
            for practice_object in practice_objects:
                practice_cursor += 1
                if practice_object.__module__ == module:
                    practice_index = practice_cursor
                    break
            if practice_index >= 0:
                practice_objects.pop(practice_index)
