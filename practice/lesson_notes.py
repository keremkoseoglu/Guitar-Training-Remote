"""Lesson notes module
This module brings up a random lesson defined in config.json
"""

from copy import deepcopy
import os
from random import choice, randint
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
import config


class LessonNotes(AbstractPractice):
    """Lesson notes exercise class"""

    _TITLE = "Lesson notes"
    _SUBTITLE = "Re-study lesson file"

    @property
    def category(self) -> PracticeCategory:
        """Returns the category of the practice"""
        return PracticeCategory.EDUCATION

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """Returns lazy fingers exercises"""
        random_steps = []
        fconfig = config.get_configuration()
        note_types = [0, 1]
        files_copy = deepcopy(fconfig["lesson_notes"]["files"])
        appended_files = []

        for quantity_pos in range(quantity):  # pylint: disable=W0612
            random_note_type = choice(note_types)

            if random_note_type == 0:
                file_count = len(files_copy)
                if file_count <= 0:
                    random_note_type = 1
                else:
                    random_file = files_copy.pop(randint(0, file_count))

            if random_note_type == 1:
                random_folder = choice(fconfig["lesson_notes"]["folders"])
                random_file = LessonNotes._get_random_file_in_folder(random_folder)

            if random_file == "":
                continue

            if random_file in appended_files:
                continue
            appended_files.append(random_file)

            random_step = exercise_step.ExerciseStep("Study file")

            random_step.helpers = [
                ExerciseHelper(
                    ExerciseHelperType.OS_COMMAND, {"command": f'open "{random_file}"'}
                )
            ]

            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE, self._SUBTITLE, random_steps, practice_category=self.category
        )

        return output

    @staticmethod
    def _get_random_file_in_folder(folder_path):
        """Returns a random file from the given folder.
        Args: folder_path: The path to the folder.
        Returns: The path to the random file.
        """
        files = os.listdir(folder_path)
        random_file = choice(files)
        return os.path.join(folder_path, random_file)
