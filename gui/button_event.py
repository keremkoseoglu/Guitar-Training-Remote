class ButtonEvent:

    def __init__(self):
        self._handlers = []

    def add_handler(self, handler):
        self._handlers.append(handler)

    def button_clicked(self, button: int):
        for handler in self._handlers:
            handler(button)
