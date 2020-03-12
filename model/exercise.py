class Exercise:

    def __init__(self, title:str, description:str, steps=None):
        self.title = title
        self.description = description

        if steps is None:
            self.steps = []
        else:
            self.steps = steps