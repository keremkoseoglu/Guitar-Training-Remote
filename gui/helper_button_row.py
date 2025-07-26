""" Helper button row module """
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class HelperButtonRow(GridLayout):
    """ Helper button row """

    _BUTTON_COUNT = 5

    def __init__(self, **kwargs):
        super(HelperButtonRow, self).__init__(**kwargs)

        self._buttons = []
        for b in range(0, self._BUTTON_COUNT): # pylint: disable=C0103, W0612
            button = Button()
            button.bind(on_press=self._button_clicked) # pylint: disable=E1101
            button.size_hint = (1/self._BUTTON_COUNT, 1)
            self._buttons.append(button)

        self.cols = self._BUTTON_COUNT
        for button in self._buttons:
            self.add_widget(button)

        self._helper_params = {}

    def apply_helper(self, params: {}):
        """ Applies button helper """
        self._helper_params = params
        self.reset_buttons()
        button_index = -1
        for param_button in self._helper_params["buttons"]:
            button_index += 1
            if button_index >= self._BUTTON_COUNT:
                return
            gui_button = self._buttons[button_index]
            gui_button.text = param_button["text"]

    def reset_buttons(self):
        """ Reset buttons """
        for button in self._buttons:
            button.text = ""

    def _button_clicked(self, instance):
        for param_button in self._helper_params["buttons"]:
            if param_button["text"] != instance.text:
                continue
            param_button["callback"](args=param_button["args"])
