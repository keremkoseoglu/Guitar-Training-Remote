""" Button row module """
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from gui.button_event import ButtonEvent


class ButtonRow(GridLayout):
    """ Button row """
    BUTTON_RESTART = 1
    BUTTON_NEXT = 4

    def __init__(self, **kwargs):
        super(ButtonRow, self).__init__(**kwargs)

        self._btn_restart = Button()
        self._btn_restart.text = "Restart"
        self._btn_restart.bind(on_press=self._btn_restart_clicked) # pylint: disable=E1101
        self._btn_restart.size_hint = (0.2, 1)

        self._btn_next = Button()
        self._btn_next.text = "Next >"
        self._btn_next.bind(on_press=self._btn_next_clicked) # pylint: disable=E1101
        self._btn_next.size_hint = (0.8, 1)

        self.cols = 2
        self.add_widget(self._btn_restart)
        self.add_widget(self._btn_next)

        self._event = ButtonEvent()

    def add_event_listener(self, handler):
        """ Add new event listener """
        self._event.add_handler(handler)

    def set_next_enabled(self, enabled: bool):
        """ Enable or disable next button """
        self._btn_next.disabled = not enabled

    def _btn_next_clicked(self, instance): # pylint: disable=W0613
        self._event.button_clicked(self.BUTTON_NEXT)

    def _btn_restart_clicked(self, instance): # pylint: disable=W0613
        self._event.button_clicked(self.BUTTON_RESTART)
