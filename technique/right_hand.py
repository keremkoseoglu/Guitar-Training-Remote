import random

class RightHand:

    def __init__(self):
        self._techniques = [
            "4 finger gallop",
            "Index mid index",
            "3 finger scale",
            "Chr. seesaw",
            "String crossing"
        ]

    def _clone_techniques(self) -> []:
        output = []
        for i in range(0, len(self._techniques)):
            output.append(self._techniques[i])
        return output

    def get_random_techniques(self, count) -> []:
        output = []
        local_tech = self._clone_techniques()
        for i in range(0, count):
            if len(local_tech) == 0:
                break
            random_tech_index = random.randint(0, len(local_tech) - 1)
            random_tech = local_tech.pop(random_tech_index)
            output.append(random_tech)
        return output