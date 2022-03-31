""" Metronome GUI module """
from os import path, getcwd
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from config import get_configuration


class Metronome(GridLayout):
    """ Metronome GUI """

    _AUDIO_DIR = "audio"
    _METRONOME_DIR = "metronome"
    _CLICK_EXTENSION = "mp3"
    _CLICK_PREFIX = "click"
    _CLICK_SEPARATOR = "_"
    _BPM_STEP = 5
    _BPM_LOW = 40
    _BPM_HIGH = 160


    def __init__(self, **kwargs):
        super(Metronome, self).__init__(**kwargs)

        self._config = get_configuration()
        self._bpm = self._config["default_bpm"]
        self._playing = False
        self._click = self._load_bpm_file()

        #self._metronome_label = Label()
        #self._metronome_label.text = "Metronome"

        self._btn_decrease = Button()
        self._btn_decrease.text = "-"
        self._btn_decrease.bind(on_press=self._btn_decrease_clicked) # pylint: disable=E1101

        self._btn_decrease2 = Button()
        self._btn_decrease2.text = "--"
        self._btn_decrease2.bind(on_press=self._btn_decrease2_clicked) # pylint: disable=E1101

        self._btn_decrease3 = Button()
        self._btn_decrease3.text = "<<"
        self._btn_decrease3.bind(on_press=self._btn_decrease3_clicked) # pylint: disable=E1101

        self._bpm_label = Label()
        self._refresh_bpm_label()

        self._btn_play = Button()
        self._btn_play.text = "Play/Stop"
        self._btn_play.bind(on_press=self._btn_play_clicked) # pylint: disable=E1101

        self._btn_increase = Button()
        self._btn_increase.text = "+"
        self._btn_increase.bind(on_press=self._btn_increase_clicked) # pylint: disable=E1101

        self._btn_increase2 = Button()
        self._btn_increase2.text = "++"
        self._btn_increase2.bind(on_press=self._btn_increase2_clicked) # pylint: disable=E1101

        self._btn_increase3 = Button()
        self._btn_increase3.text = ">>"
        self._btn_increase3.bind(on_press=self._btn_increase3_clicked) # pylint: disable=E1101

        self.cols = 8
        #self.add_widget(self._metronome_label)
        self.add_widget(self._btn_decrease3)
        self.add_widget(self._btn_decrease2)
        self.add_widget(self._btn_decrease)
        self.add_widget(self._bpm_label)
        self.add_widget(self._btn_play)
        self.add_widget(self._btn_increase)
        self.add_widget(self._btn_increase2)
        self.add_widget(self._btn_increase3)

    @property
    def bpm(self) -> int:
        """ BPM value """
        return self._bpm

    @bpm.setter
    def bpm(self, value: int):
        """ BPM value """
        self._change_bpm(value - self._bpm)

    def start(self):
        """ Starts metronome """
        if self._playing:
            return
        self._click = self._load_bpm_file()
        self._click.play()
        self._playing = True

    def stop(self):
        """ Stops metronome """
        if not self._playing:
            return
        self._click.stop()
        self._playing = False

    def reset(self):
        """ Stops and resets the metronome """
        self.stop()
        self.bpm = self._config["default_bpm"]

    def _btn_decrease_clicked(self, instance): # pylint: disable=W0613
        self._change_bpm(Metronome._BPM_STEP * -1)

    def _btn_decrease2_clicked(self, instance): # pylint: disable=W0613
        self._change_bpm(Metronome._BPM_STEP * -2)

    def _btn_decrease3_clicked(self, instance): # pylint: disable=W0613
        self._set_bpm(Metronome._BPM_LOW)

    def _btn_increase_clicked(self, instance): # pylint: disable=W0613
        self._change_bpm(Metronome._BPM_STEP)

    def _btn_increase2_clicked(self, instance): # pylint: disable=W0613
        self._change_bpm(Metronome._BPM_STEP * 2)

    def _btn_increase3_clicked(self, instance): # pylint: disable=W0613
        self._set_bpm(Metronome._BPM_HIGH)

    def _change_bpm(self, delta: int):
        new_bpm = self._bpm + delta
        if new_bpm < Metronome._BPM_LOW:
            new_bpm = int(new_bpm * 4)
        if new_bpm > Metronome._BPM_HIGH:
            new_bpm = int(new_bpm / 2)
        self._set_bpm(new_bpm)

    def _set_bpm(self, bpm: int):
        self._click.stop()
        self._click.unload()
        self._bpm = bpm
        remain = self._bpm % 5
        if remain in (1, 2):
            while self._bpm %5 != 0:
                self._bpm -= 1
        elif remain in (3, 4):
            while self._bpm %5 != 0:
                self._bpm += 1

        self._refresh_bpm_label()
        if self._playing:
            self.stop()
            self.start()

    def _btn_play_clicked(self, instance): # pylint: disable=W0613
        if self._playing:
            self.stop()
        else:
            self.start()

    def _refresh_bpm_label(self):
        self._bpm_label.text = f"{str(self._bpm)}  BPM"

    def _load_bpm_file(self) -> SoundLoader:
        file_name = Metronome._CLICK_PREFIX + Metronome._CLICK_SEPARATOR + str(self._bpm)
        file_name += "." + Metronome._CLICK_EXTENSION
        file_path = path.join(getcwd(), Metronome._AUDIO_DIR, Metronome._METRONOME_DIR, file_name)
        return SoundLoader.load(file_path)
