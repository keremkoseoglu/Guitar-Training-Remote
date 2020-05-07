from model import exercise, exercise_step
from model.guitar import Guitar
from music_theory import chord
from practice import abstract_practice
import random


class ScaleOnChord(abstract_practice.AbstractPractice):
    _TITLE = "Scale on chord"
    _SUBTITLE = "a scale on top of chord"
    _PLAY_CHOICE = ["Play in", "Play out"]

    def get_exercise(self, quantity: int, guitar: Guitar) -> exercise.Exercise:
        random_steps = []
        random_chords = chord.Chord().get_random_chords(quantity)

        for random_chord in random_chords:
            random_step = exercise_step.ExerciseStep(
                random_chord,
                super(ScaleOnChord, self).get_random_position_suggestion_text()
            )

            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._get_subtitle(), random_steps)
        return output

    def _get_random_play_choice(self) -> str:
        random_choice = random.randint(0, len(ScaleOnChord._PLAY_CHOICE) - 1)
        return ScaleOnChord._PLAY_CHOICE[random_choice]

    def _get_subtitle(self) -> str:
        return self._get_random_play_choice() + " " + ScaleOnChord._SUBTITLE
