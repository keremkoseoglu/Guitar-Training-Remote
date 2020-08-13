""" Category balance based generator """
import random
from config import get_configuration
from factory import  all_practices, some_practices
from model import workout
from model.guitar import get_random_guitar
from practice.practice_category import PracticeCategory

class CategoryBalance(some_practices.SomePractices):
    """ All practices """
    def __init__(self):
        super().__init__()
        self._select_guitar = True
        self.guitar = {}
        self._config = get_configuration()

    def get_workout(self, guitar: dict = None) -> workout.WorkOut:
        """ Returns a new workout containing all practices """
        if self._select_guitar:
            self.guitar = get_random_guitar()
        else:
            self.guitar = guitar

        tmp_categories = []
        for practice_category in PracticeCategory:
            tmp_categories.append(practice_category.name)
        categories = {}
        while len(tmp_categories) > 0:
            cat_index = random.randint(0, len(tmp_categories)-1)
            tmp_category = tmp_categories.pop(cat_index)
            categories[tmp_category] = []

        everything = all_practices.AllPractices().get_workout(self.guitar)
        for exercise in everything.exercises:
            categories[exercise.practice_category.name].append(exercise)

        exercise_count = random.randint(
            self._config["practice_selection"]["min_practice_count"],
            self._config["practice_selection"]["max_practice_count"])

        exercise_per_category = round(exercise_count / len(categories))
        output_exercises = []

        for category in categories:
            exercises = categories[category]
            for i in range(0, exercise_per_category): # pylint: disable=W0612
                if len(exercises) <= 0:
                    break
                random_index = random.randint(0, len(exercises) - 1)
                random_exercise = exercises.pop(random_index)
                output_exercises.append(random_exercise)

        output = workout.WorkOut(output_exercises)

        if self._select_guitar:
            output.add_guitar(self.guitar)
        return output

    def set_select_guitar(self, select: bool):
        """ Do we need to select a guitar """
        self._select_guitar = select
