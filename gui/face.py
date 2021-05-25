""" Main entry point """
import webbrowser
from typing import List
import os
import subprocess
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from factory.category_balance import CategoryBalance
from gui.button_row import ButtonRow
from gui.helper_button_row import HelperButtonRow
from gui.metronome import Metronome
from model.exercise_helper import ExerciseHelperType, ExerciseHelper, get_flukebox_helper
import config

_APP_TITLE = "Guitar Training Remote"

class Face(GridLayout):
    """ Main form """

    _H1_FONT_SIZE = 100
    _H2_FONT_SIZE = 24
    _H3_FONT_SIZE = 18

    def __init__(self, **kwargs):
        super(Face, self).__init__(**kwargs)

        # --- Prepare GUI elements -----

        self._exercise_main_label = Label()
        self._exercise_main_label.text = "Test"
        self._exercise_main_label.font_size = str(self._H2_FONT_SIZE) + "dp"
        self._exercise_main_label.size_hint = (1, 0.1)

        self._exercise_sub_label = Label()
        self._exercise_sub_label.text = "Test"
        self._exercise_sub_label.font_size = str(self._H3_FONT_SIZE) + "dp"
        self._exercise_sub_label.size_hint = (1, 0.1)

        self._step_main_label = Label()
        self._step_main_label.text = "Test"
        self._step_main_label.font_size = str(self._H1_FONT_SIZE) + "dp"
        self._step_main_label.size_hint = (1, 0.5)

        self._step_sub_label = Label()
        self._step_sub_label.text = "Test"
        self._step_sub_label.font_size = str(self._H3_FONT_SIZE) + "dp"
        self._step_sub_label.size_hint = (1, 0.1)

        self._stop_watch_label = Label()
        self._stop_watch_label.size_hint = (1, 0.1)

        self._buttons = ButtonRow()
        self._buttons.size_hint = (1, 0.1)
        self._buttons.add_event_listener(self._handle_button_click)

        self._helper_buttons = HelperButtonRow()
        self._helper_buttons.size_hint = (1, 0.05)

        self._metronome = Metronome()
        self._metronome.size_hint = (1, 0.05)

        self.cols = 1
        self.add_widget(self._exercise_main_label)
        self.add_widget(self._exercise_sub_label)
        self.add_widget(self._step_main_label)
        self.add_widget(self._step_sub_label)
        self.add_widget(self._stop_watch_label)
        self.add_widget(self._helper_buttons)
        self.add_widget(self._metronome)
        self.add_widget(self._buttons)

        # --- Start workout -----

        self._workout = None
        self._exercise_step_tick_count = 0
        self._guitar_selected = False
        self._open_guitar_apps = False
        self._guitar = {}
        self._restart()

    def _handle_button_click(self, button: int):
        self._metronome.reset()
        if button == ButtonRow.BUTTON_NEXT:
            self.next_step()
        elif button == ButtonRow.BUTTON_RESTART:
            self._restart()
        elif button == ButtonRow.BUTTON_REPICK:
            self._restart(repick=True)
        elif button == ButtonRow.BUTTON_CONFIG:
            config.edit_configuration()

    def next_step(self):
        """ Goes to the next step """
        prev_exercise_index = self._workout.get_exercise_index()
        try:
            next_exer, next_step = self._workout.get_next_step()
        except Exception:
            return

        if next_exer is None or next_step is None:
            self._buttons.set_next_enabled(False)
            self._exercise_main_label.text = ""
            self._exercise_sub_label.text = ""
            self._step_main_label.text = "Finished!"
            self._step_sub_label.text = "Now play freestyle for fun!"

            flukebox = get_flukebox_helper("final_playlist")
            if flukebox is not None:
                self._process_helpers([flukebox])

        else:
            if prev_exercise_index != self._workout.get_exercise_index():
                self._helper_buttons.reset_buttons()
                self._paint_exercise()
            self._paint_exercise_step()
            self._refresh_status_text()

        if self._open_guitar_apps:
            self._open_guitar_apps = False
            for app in self._guitar["apps"]:
                subprocess.call(["open", app])

    def set_step_sub_label_text(self, text: str):
        """ Alt metni günceller """
        self._step_sub_label.text = text

    def _paint_exercise(self):
        exe = self._workout.get_current_exercise()
        self._exercise_main_label.text = exe.title
        self._exercise_sub_label.text = exe.description
        self._process_helpers(exe.helpers)

    def _paint_exercise_step(self):
        step = self._workout.get_current_step()
        self._step_main_label.text = step.main_text
        self._step_sub_label.text = str(step.sub_text)
        self._process_helpers(step.helpers)

    def _refresh_status_text(self):
        try:
            status_text = \
                "Lesson " + str(self._workout.get_exercise_index() + 1) \
                + " / " + str(self._workout.get_exercise_count())

            status_text += \
                ", step " + str(self._workout.get_step_index() + 1) \
                + " / " + str(self._workout.get_step_count())
        except Exception:
            status_text = ""

        self._stop_watch_label.text = status_text

    def _restart(self, repick=False):
        practice_obj = CategoryBalance()
        if self._guitar_selected and (not repick):
            practice_obj.set_select_guitar(False)
            self._workout = practice_obj.get_workout(self._guitar)
        else:
            practice_obj.set_select_guitar(True)
            self._guitar_selected = True
            self._workout = practice_obj.get_workout()
            self._open_guitar_apps = True

        self._exercise_step_tick_count = -1
        self._paint_exercise()
        self._paint_exercise_step()
        self._buttons.set_next_enabled(True)
        self._refresh_status_text()
        self._guitar = practice_obj.guitar

    def _process_helpers(self, helpers: List[ExerciseHelper]):
        for helper in helpers:
            if helper.helper_type == ExerciseHelperType.BROWSER:
                webbrowser.open(helper.params["url"])
            elif helper.helper_type == ExerciseHelperType.METRONOME:
                self._metronome.bpm = helper.params["bpm"]
            elif helper.helper_type == ExerciseHelperType.OS_COMMAND:
                os.system(helper.params["command"])
            elif helper.helper_type == ExerciseHelperType.BUTTONS:
                self._helper_buttons.apply_helper(helper.params)


class FaceFactory:
    """ Singleton for face """
    _FACE: Face = None

    @staticmethod
    def get_singleton() -> Face:
        """ Returns singleton instance """
        if FaceFactory._FACE is None:
            FaceFactory._FACE = Face()
        return FaceFactory._FACE


class GtrApp(App):
    """ Main application """
    def build(self):
        """ Builds application """
        self.title = _APP_TITLE
        return FaceFactory.get_singleton()
