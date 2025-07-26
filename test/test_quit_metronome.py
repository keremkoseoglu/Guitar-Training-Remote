""" Test methods """
import subprocess
from model.exercise_helper import get_external_metronome_helper, quit_metronome

def test_quit_metronome():
    """ Test quit metronome """
    metro_helper = get_external_metronome_helper(100)
    subprocess.Popen(metro_helper.params["command"], shell=True)
    quit_metronome()
