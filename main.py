""" Program entry point """
import gui.face
# from practice.double_thumb import DoubleThumb

if __name__ == "__main__":
    """
    ks = DoubleThumb()
    bass = { "type": "J Bass",
             "kind": "instrument",
             "strings": 4,
             "octaves": 4,
             "from": 0,
             "to": 20,
             "apps": [] }
    exercise = ks.get_exercise(20, bass)
    print(exercise) """
    gui.face.GtrApp().run()
