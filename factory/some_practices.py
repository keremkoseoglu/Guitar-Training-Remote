""" All practices """

import random
from typing import List
from config import get_configuration
from factory import all_practices
from model import workout
from model.guitar import get_random_guitar


class SomePractices:
    """All practices
    PROTOCOL: AbstractFactory
    """

    def __init__(self):
        super().__init__()
        self._select_guitar = True
        self.guitar = {}
        self._config = get_configuration()

    def get_workout(
        self, guitar: dict = None, exclude_classes: List[str] = None
    ) -> workout.WorkOut:
        """Returns a new workout containing all practices"""
        if self._select_guitar:
            self.guitar = get_random_guitar()
        else:
            self.guitar = guitar

        output = all_practices.AllPractices().get_workout(
            self.guitar, exclude_classes=exclude_classes
        )

        remain_count = random.randint(
            self._config["practice_selection"]["min_practice_count"],
            self._config["practice_selection"]["max_practice_count"],
        )

        output.remove_random_exercises(
            remain_count, self._config["practice_selection"]["must_select"]
        )

        if self._select_guitar:
            output.add_guitar(self.guitar)
        return output

    def set_select_guitar(self, select: bool):
        """Do we need to select a guitar"""
        self._select_guitar = select
