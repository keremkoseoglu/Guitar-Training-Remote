""" Category balance based generator """
import random
from config import get_configuration
from factory import  all_practices, some_practices
from model import workout
from model.guitar import get_random_guitar
from practice.practice_category import PracticeCategory, get_category_group

class CategoryBalance(some_practices.SomePractices):
    """ Balanced category practices """
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

        tmp_groups = []
        for practice_category in PracticeCategory:
            group_name = get_category_group(practice_category).name
            if group_name not in tmp_groups:
                tmp_groups.append(group_name)
        groups = {}
        while len(tmp_groups) > 0:
            cat_index = random.randint(0, len(tmp_groups)-1)
            tmp_group = tmp_groups.pop(cat_index)
            groups[tmp_group] = []

        everything = all_practices.AllPractices().get_workout(self.guitar)
        for exercise in everything.exercises:
            if exercise is None:
                continue
            groups[get_category_group(exercise.practice_category).name].append(exercise)

        exercise_count = random.randint(
            self._config["practice_selection"]["min_practice_count"],
            self._config["practice_selection"]["max_practice_count"])

        exercise_per_group = round(exercise_count / len(groups))
        output_exercises = []

        for group in groups:
            exercises = groups[group]
            for i in range(0, exercise_per_group): # pylint: disable=W0612
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
