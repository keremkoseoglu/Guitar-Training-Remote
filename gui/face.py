import datetime
from factory import some_practices
from gui.button_event import ButtonEvent
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from model import exercise, exercise_step

_APP_TITLE = "Guitar Training Remote"

class ButtonRow(GridLayout):

    BUTTON_RESTART = 1
    BUTTON_NEXT = 4

    def __init__(self, **kwargs):
        super(ButtonRow, self).__init__(**kwargs)

        self._btn_restart = Button()
        self._btn_restart.text = "Restart"
        self._btn_restart.bind(on_press=self._btn_restart_clicked)
        self._btn_restart.size_hint = (0.2, 1)

        self._btn_next = Button()
        self._btn_next.text = "Next >"
        self._btn_next.bind(on_press=self._btn_next_clicked)
        self._btn_next.size_hint = (0.8, 1)

        self.cols = 2
        self.add_widget(self._btn_restart)
        self.add_widget(self._btn_next)

        self._event = ButtonEvent()

    def add_event_listener(self, handler):
        self._event.add_handler(handler)

    def set_next_enabled(self, enabled: bool):
        self._btn_next.disabled = not enabled

    def _btn_next_clicked(self, instance):
        self._event.button_clicked(self.BUTTON_NEXT)

    def _btn_restart_clicked(self, instance):
        self._event.button_clicked(self.BUTTON_RESTART)

class Face(GridLayout):

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

        self.cols = 1
        self.add_widget(self._exercise_main_label)
        self.add_widget(self._exercise_sub_label)
        self.add_widget(self._step_main_label)
        self.add_widget(self._step_sub_label)
        self.add_widget(self._stop_watch_label)
        self.add_widget(self._buttons)

        # --- Start workout -----

        self._workout = None
        self._exercise_step_tick_count = 0
        self._guitar_selected = False
        self._restart()

    def _handle_button_click(self, button: int):
        if button == ButtonRow.BUTTON_NEXT:
            self._next_step()
        elif button == ButtonRow.BUTTON_RESTART:
            self._restart()

    def _next_step(self):

        try:
            next_exer, next_step = self._workout.get_next_step()
        except:
            return

        if next_exer is None or next_step is None:
            self._buttons.set_next_enabled(False)
            self._exercise_main_label.text = ""
            self._exercise_sub_label.text = ""
            self._step_main_label.text = "Finished!"
            self._step_sub_label.text = ""
        else:
            self._paint_exercise()
            self._paint_exercise_step()
            self._refresh_status_text()

    def _paint_exercise(self):
        exe = self._workout.get_current_exercise()
        self._exercise_main_label.text = exe.title
        self._exercise_sub_label.text = exe.description
        pass

    def _paint_exercise_step(self):
        step = self._workout.get_current_step()
        self._step_main_label.text = step.main_text
        self._step_sub_label.text = str(step.sub_text)

    def _refresh_status_text(self):

        try:
            status_text = \
                "Lesson " + str(self._workout.get_exercise_index() + 1) \
                + " / " + str(self._workout.get_exercise_count())

            status_text += \
                ", step " + str(self._workout.get_step_index() + 1) \
                + " / " + str(self._workout.get_step_count())
        except:
            status_text = ""

        self._stop_watch_label.text = status_text

    def _restart(self):
        practice_obj = some_practices.SomePractices()
        if self._guitar_selected:
            practice_obj.set_select_guitar(False)
        else:
            practice_obj.set_select_guitar(True)
            self._guitar_selected = True

        self._workout = practice_obj.get_workout()
        self._exercise_step_tick_count = -1
        self._paint_exercise()
        self._paint_exercise_step()
        self._buttons.set_next_enabled(True)
        self._refresh_status_text()


class GtrApp(App):
    def build(self):
        self.title = _APP_TITLE
        return Face()