""" Key signature quiz """
import random
from typing import List
import webbrowser
from model import exercise, exercise_step
from model.exercise_helper import ExerciseHelperType, ExerciseHelper
from music_theory import key_signature
from practice import abstract_practice
from practice.practice_category import PracticeCategory

class KeySignatureQuiz(abstract_practice.AbstractPractice):
    """ Key signature quiz """
    _TITLE = "Key signature quiz"
    _SUBTITLE = "Answer the following questions"
    _BUTTON_START = "start"

    def __init__(self):
        self._key_sig = key_signature.KeySignature()

    @property
    def category(self) -> PracticeCategory:
        """ Returns the category of the practice """
        return PracticeCategory.THEORY

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        """ Returns the exercise object """
        random_steps = []

        for step_index in range(0, quantity): # pylint: disable=W0612
            step_text = ""

            quiz_type = random.randint(0, 2)

            if quiz_type == 0: # How many flats does Cm have
                chord, oddity = self._key_sig.get_random_chord_and_oddity()
                step_text = f"? {oddity} in {chord}"
            elif quiz_type == 1: # Which maj has 2 flats
                chord_type = self._key_sig.get_random_chord_type()
                oddity_cnt = str(self._key_sig.get_random_oddity_count())
                oddity = self._key_sig.get_random_oddity()
                step_text = f"? {chord_type} has {oddity_cnt} {oddity}"
            elif quiz_type == 2: # Name maj chords containing C
                chord_type = self._key_sig.get_random_chord_type()
                odd_note = self._key_sig.get_random_odd_node()
                step_text = f"? {chord_type} has {odd_note}"

            random_step = exercise_step.ExerciseStep(step_text)
            random_steps.append(random_step)

        output = exercise.Exercise(
            self._TITLE,
            self._SUBTITLE,
            random_steps,
            practice_category=self.category)

        output.helpers = self._produce_helpers()

        return output

    def _produce_helpers(self) -> List[ExerciseHelper]:
        helper = ExerciseHelper(
            ExerciseHelperType.BUTTONS,
            {"buttons": [
                {
                    "text": "Start",
                    "callback": self.helper_clicked,
                    "args": {"button": self._BUTTON_START}
                }
            ]}
        )
        return [helper]

    def helper_clicked(self, args: dict):
        """ Called when the helper button is clicked """
        if args["button"] == KeySignatureQuiz._BUTTON_START:
            webbrowser.open(self._key_sig.url)
