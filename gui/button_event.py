""" Button click event """

class ButtonEvent:
    """ Button click event """

    def __init__(self):
        self._handlers = []

    def add_handler(self, handler):
        """ Adds event handler """
        self._handlers.append(handler)

    def button_clicked(self, button: int):
        """ Button click event """
        for handler in self._handlers:
            handler(button)
