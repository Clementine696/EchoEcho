import pyaudio
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import numpy as np

class MicrophoneAudioWaveform:
    def __init__(self):
        # initialize pyaudio
        self.p = pyaudio.PyAudio()

        # define audio stream parameters
        self.CHUNK = 1024 * 4   # number of audio frames per buffer
        self.FORMAT = pyaudio.paInt16  # audio format
        self.CHANNELS = 1  # mono audio
        self.RATE = 44100  # audio sampling rate

        # create audio stream
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        # create plot window
        self.app = QApplication([])
        self.win = pg.GraphicsLayoutWidget(show = True)
        # self.win = pg.GraphicsLayoutWidget(show=False)
        self.plot = self.win.addPlot()
        self.plot.setYRange(-5000, 5000)
        self.curve = self.plot.plot()

        # set up a timer to regularly update the plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(0)

    # function to update plot data
    def update_plot(self):
        data = self.stream.read(self.CHUNK)
        data_int = np.frombuffer(data, dtype=np.int16)
        self.curve.setData(data_int)
        QApplication.processEvents()

    # start Qt event loop
    def run(self):
        self.app.exec_()

    # stop audio stream and terminate pyaudio
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()  

if __name__ == '__main__':
    # create instance of MicrophoneAudioWaveform class
    waveform = MicrophoneAudioWaveform()
    waveform.run()
    waveform.stop()
