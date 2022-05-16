""" Program entry point """
import gui.face
from practice.metronome_style import MetronomeStyle

def run_app():
    """ Main """
    gui.face.GtrApp().run()

def test_app():
    """ Test """
    test_exercise = MetronomeStyle()
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
