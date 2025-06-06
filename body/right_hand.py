""" Right hand techniques """
import random
from config import get_configuration


class RightHand:
    """Right hand techniques"""

    def __init__(self):
        config = get_configuration()
        self._techniques = config["right_hand_exercises"]

    def _clone_techniques(self) -> []:
        output = []
        for i in range(0, len(self._techniques)):
            output.append(self._techniques[i])
        return output

    def get_random_techniques(self, count) -> []:
        """Returns random right hand techniques"""
        output = []
        local_tech = self._clone_techniques()
        for i in range(0, count):  # pylint: disable=W0612
            if len(local_tech) == 0:
                break
            random_tech_index = random.randint(0, len(local_tech) - 1)
            random_tech = local_tech.pop(random_tech_index)
            output.append(random_tech)
        return output
