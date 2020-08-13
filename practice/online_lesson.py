""" Online lesson module """
from typing import List
import webbrowser
from copy import copy
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from practice.abstract_practice import AbstractPractice
from practice.practice_category import PracticeCategory
from config import get_configuration, save_configuration
from gui.face import FaceFactory


class OnlineLesson(AbstractPractice):
    """ Online lesson class """

    _TITLE = "Online lesson"
    _SUBTITLE = "Take an online lesson"
    _BUTTON_START = "start"
    _BUTTON_REMOVE = "remove"
    _BUTTON_REQUEUE = "requeue"

    def __init__(self):
        self._config = get_configuration()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.EDUCATION

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns random online lesson """
        if guitar["kind"] != "instrument":
            return None
        if "online_lessons" not in self._config:
            return None
        if len(self._config["online_lessons"]) <= 0:
            return None

        lesson = self._current_lesson
        step = exercise_step.ExerciseStep(lesson["name"], lesson["url"])
        steps = [step]
        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            steps,
            practice_category=self.category)
        output.helpers = self._produce_helpers()
        return output

    def helper_clicked(self, args: dict):
        """ Called when the helper button is clicked """
        face = FaceFactory.get_singleton()
        lesson = self._current_lesson

        if args["button"] == OnlineLesson._BUTTON_START:
            webbrowser.open(lesson["url"])

        if args["button"] == OnlineLesson._BUTTON_REMOVE:
            self._config["online_lessons"].pop(self._current_lesson_index)
            save_configuration()
            face.next_step()

        if args["button"] == OnlineLesson._BUTTON_REQUEUE:
            lesson_copy = copy(lesson)
            self._config["online_lessons"].pop(self._current_lesson_index)
            self._config["online_lessons"].append(lesson_copy)
            save_configuration()
            face.next_step()

    @property
    def _current_lesson(self) -> dict:
        return self._config["online_lessons"][self._current_lesson_index]

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
                    "args": {"button": OnlineLesson._BUTTON_START}
                },
                {
                    "text": "Remove",
                    "callback": self.helper_clicked,
                    "args": {"button": OnlineLesson._BUTTON_REMOVE}
                },
                {
                    "text": "Requeue",
                    "callback": self.helper_clicked,
                    "args": {"button": OnlineLesson._BUTTON_REQUEUE}
                }
            ]}
        )
        return [helper]
