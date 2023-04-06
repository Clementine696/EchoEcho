import sys
import numpy as np
import pyaudio
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class RealTimeVoicePlot(QWidget):
    def __init__(self, parent=None):
        super(RealTimeVoicePlot, self).__init__(parent)
        self.setWindowTitle('Real Time Voice Plot')
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 1024)
        self.ax.set_ylim(-32768, 32768)
        self.line, = self.ax.plot([], [])

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

        # set up a timer to regularly update the plot
        self.timer = self.canvas.new_timer(interval=10)
        self.timer.add_callback(self.update_plot)
        self.timer.start()

    def update_plot(self):
        data = self.stream.read(self.CHUNK)
        data_int = np.frombuffer(data, dtype=np.int16)
        self.line.set_data(np.arange(len(data_int)), data_int)
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    real_time_voice_plot = RealTimeVoicePlot()
    real_time_voice_plot.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
