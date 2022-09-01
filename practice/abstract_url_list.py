""" URL list lesson module """
from typing import List
import webbrowser
from copy import copy
import pyperclip
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from config import get_configuration, save_configuration
from gui.face import FaceFactory
from performance.advice import Advice


class AbstractUrlList(AbstractPractice):
    """ URL list class
    Technically this is not an abstract class, but logically it is
    """

    _BUTTON_START = "start"
    _BUTTON_REMOVE = "remove"
    _BUTTON_REQUEUE = "requeue"
    _BUTTON_PASTE_URL = "paste"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.EDUCATION

    @property
    def _title(self) -> str:
        return ""

    @property
    def _subtitle(self) -> str:
        return ""

    @property
    def _config_section(self) -> str:
        return ""

    @staticmethod
    def _is_guitar_eligible(guitar: dict) -> bool:
        return guitar is not None

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random online lesson """
        if guitar["kind"] != "instrument":
            return None
        if not AbstractUrlList._is_guitar_eligible(guitar):
            return None
        if self._config_section not in self._config:
            return None
        if len(self._config[self._config_section]) <= 0:
            return None

        lesson = self._current_lesson
        sub_txt = Advice().get_random_advice()
        step = exercise_step.ExerciseStep(lesson["name"], sub_txt)
        steps = [step]
        output = exercise.Exercise(
            self._title,
            self._subtitle,
            steps,
            practice_category=self.category)
        output.helpers = self._produce_helpers()
        return output

    def helper_clicked(self, args: dict):
        """ Called when the helper button is clicked """
        face = FaceFactory.get_singleton()
        lesson = self._current_lesson

        if args["button"] == AbstractUrlList._BUTTON_START:
            webbrowser.open(lesson["url"])

        if args["button"] == AbstractUrlList._BUTTON_REMOVE:
            self._config[self._config_section].pop(self._current_lesson_index)
            save_configuration()
            face.next_step()

        if args["button"] == AbstractUrlList._BUTTON_REQUEUE:
            lesson_copy = copy(lesson)
            self._config[self._config_section].pop(self._current_lesson_index)
            self._config[self._config_section].append(lesson_copy)
            save_configuration()
            face.next_step()

        if args["button"] == AbstractUrlList._BUTTON_PASTE_URL:
            new_url = pyperclip.paste()
            if new_url != "":
                self._config[self._config_section][self._current_lesson_index]["url"] = new_url
                save_configuration()
                face.set_step_sub_label_text(new_url)

    @property
    def _current_lesson(self) -> dict:
        return self._config[self._config_section][self._current_lesson_index]

    @property
    def _current_lesson_index(self) -> int:
        return 0

    def _produce_helpers(self) -> List[ExerciseHelper]:
        helper = ExerciseHelper(
            ExerciseHelperType.BUTTONS,
            {"buttons": [
                {
                    "text": "Start",
                    "callback": self.helper_clicked,
                    "args": {"button": self._BUTTON_START}
                },
                {
                    "text": "Remove",
                    "callback": self.helper_clicked,
                    "args": {"button": self._BUTTON_REMOVE}
                },
                {
                    "text": "Requeue",
                    "callback": self.helper_clicked,
                    "args": {"button": AbstractUrlList._BUTTON_REQUEUE}
                },
                {
                    "text": "Paste bookmark",
                    "callback": self.helper_clicked,
                    "args": {"button": AbstractUrlList._BUTTON_PASTE_URL}
                }
            ]}
        )
        return [helper]
