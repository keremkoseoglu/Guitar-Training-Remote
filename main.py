""" Program entry point """
import gui.face
from practice.improv import Improv
from config.backup import Backup
# from test.test_quit_metronome import test_quit_metronome

def run_app():
    """ Main """
    Backup().run()
    gui.face.GtrApp().run()

def test_app():
    """ Test """
    # test_quit_metronome()
    # return

    test_exercise = Improv()
    bass = {"type": "J Bass",
            "kind": "instrument",
            "strings": 4,
            "octaves": 4,
            "from": 0,
            "to": 20,
            "apps": []}
    exercise = test_exercise.get_exercise(20, bass)
    print(exercise)

if __name__ == "__main__":
    #test_app()
    run_app()
