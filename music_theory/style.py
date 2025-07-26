""" Music style module """
import random
from config import get_configuration

class Style:
    """ Music style class """
    def __init__(self):
        config = get_configuration()
        self._styles = config["styles"]

    def get_random_style(self) -> str:
        """ Returns a random style """
        style_index = random.randint(0, len(self._styles) - 1)
        return self._styles[style_index]
