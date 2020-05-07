""" All practices """
import random
from factory import abstract_factory, all_practices
from model import workout
from model.guitar import Guitar, get_random_guitar


class SomePractices(abstract_factory.AbstractFactory):
    """ All practices """
    _LOW_PERCENT = 50
    _HIGH_PERCENT = 80

    def __init__(self):
        super().__init__()
        self._select_guitar = True

    def get_workout(self, guitar: Guitar = Guitar.UNDEFINED) -> workout.WorkOut:
        """ Returns a new workout containing all practices """
        if self._select_guitar:
            random_guitar = get_random_guitar()
        else:
            random_guitar = guitar

        output = all_practices.AllPractices().get_workout(random_guitar)
        remove_percent = random.randint(self._LOW_PERCENT, self._HIGH_PERCENT)
        output.remove_random_exercies(remove_percent)

        if self._select_guitar:
            output.add_guitar(random_guitar)
        return output

    def set_select_guitar(self, select: bool):
        """ Do we need to select a guitar """
        self._select_guitar = select
