""" Button row module """
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from gui.button_event import ButtonEvent


class ButtonRow(GridLayout):
    """ Button row """
    BUTTON_RESTART = 1
    BUTTON_NEXT = 4
    BUTTON_REPICK = 5
    BUTTON_CONFIG = 6

    def __init__(self, **kwargs):
        super(ButtonRow, self).__init__(**kwargs)

        self._btn_config = Button()
        self._btn_config.text = "..."
        self._btn_config.bind(on_press=self._btn_config_clicked) # pylint: disable=E1101
        self._btn_config.size_hint = (0.05, 1)

        self._btn_repick = Button()
        self._btn_repick.text = "Repick"
        self._btn_repick.bind(on_press=self._btn_repick_clicked) # pylint: disable=E1101
        self._btn_repick.size_hint = (0.2, 1)

        self._btn_restart = Button()
        self._btn_restart.text = "Restart"
        self._btn_restart.bind(on_press=self._btn_restart_clicked) # pylint: disable=E1101
        self._btn_restart.size_hint = (0.2, 1)

        self._btn_next = Button()
        self._btn_next.text = "Next >"
        self._btn_next.bind(on_press=self._btn_next_clicked) # pylint: disable=E1101
        self._btn_next.size_hint = (0.8, 1)

        self.cols = 4
        self.add_widget(self._btn_config)
        self.add_widget(self._btn_repick)
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

    def _btn_repick_clicked(self, instance): # pylint: disable=W0613
        self._event.button_clicked(self.BUTTON_REPICK)

    def _btn_config_clicked(self, instance): # pylint: disable=W0613
        self._event.button_clicked(self.BUTTON_CONFIG)
