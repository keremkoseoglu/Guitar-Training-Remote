""" All practices """

import random
from typing import List
from vibhaga.inspector import Inspector, Container
from model import workout
from config import get_configuration


class AllPractices:  # pylint: disable=R0903
    """All practices
    PROTOCOL: AbstractFactory
    """

    def __init__(self):
        self._config = get_configuration()

    def get_workout(
            self, guitar: dict = None, exclude_classes: List[str] = None
    ) -> workout.WorkOut:
        """Returns a new workout containing all practices"""
        exercises = []
        inspector_exclude_classes = [
            "AbstractPractice",
            "AbstractUrlList",
            "PracticeCategory",
            "PracticeCategoryGroup",
            "Position",
            "Guitar",
            "SupportPractice",
            "Accent",
            "ApproachDirection",
        ]

        if exclude_classes is not None:
            for exclude_class in exclude_classes:
                inspector_exclude_classes.append(exclude_class)

        practice_objects = Inspector.get_classes_in_container(
            Container(["practice"]), ["abstract"], inspector_exclude_classes
        )

        AllPractices._delete_duplicates(practice_objects)

        if "only_select" in self._config["practice_selection"]:
            only_select = self._config["practice_selection"]["only_select"]
            if only_select != "":
                for practice_object in practice_objects:
                    if practice_object.__module__ == only_select:
                        random_step_count = self._get_random_step_count()
                        produced_exercise = practice_object().get_exercise(
                            random_step_count, guitar
                        )
                        exercises.append(produced_exercise)
                        output = workout.WorkOut(exercises)
                        return output

        if "dont_select" in self._config["practice_selection"]:
            removable_indices = []
            index = -1
            for practice_object in practice_objects:
                index += 1
                if (
                        practice_object.__module__
                        in self._config["practice_selection"]["dont_select"]
                ):
                    removable_indices.append(index)
            removable_indices.sort(reverse=True)
            for index in removable_indices:
                practice_objects.pop(index)

        while len(practice_objects) > 0:
            random_practice_index = random.randint(0, len(practice_objects) - 1)
            practice_object = practice_objects[random_practice_index]

            random_step_count = self._get_random_step_count()
            try:
                produced_exercise = practice_object().get_exercise(
                    random_step_count, guitar
                )
            except Exception:
                produced_exercise = None
            if produced_exercise is not None:
                exercises.append(produced_exercise)
            practice_objects.pop(random_practice_index)

        output = workout.WorkOut(exercises)
        return output

    def _get_random_step_count(self):
        return random.randint(
            1, self._config["practice_selection"]["max_steps_per_exercise"]
        )

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
