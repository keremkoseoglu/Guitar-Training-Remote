""" Metronome riff """
from model import exercise
from model.exercise_helper import get_flukebox_helper
from practice.metronome import Metronome

class MetronomeRiff(Metronome):
    """ Metronome riff """

    _TITLE = "Metronome riff"

    def get_exercise(self, quantity: int, guitar: dict) -> exercise.Exercise:
        output = super().get_exercise(quantity, guitar)
        output.title = MetronomeRiff._TITLE
        output.description = "Play riff over metronome"

        flukebox_helper = get_flukebox_helper("final_playlist")
        if flukebox_helper is not None:
            if output.helpers is None:
                output.helpers = []
            output.helpers.append(flukebox_helper)

        return output
