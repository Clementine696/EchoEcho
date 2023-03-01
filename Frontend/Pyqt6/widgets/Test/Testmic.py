import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# import noisereduce as nr
# import pyaudio
# import numpy as np
# import sounddevice as sd


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'EchoEcho'
        self.left = 200
        self.top = 100
        self.width = 1280
        self.height = 720
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Test Microphone', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
    #     p = pyaudio.PyAudio()

    #     # Open the input microphone stream
    #     input_stream = p.open(format=pyaudio.paInt16,
    #                       channels=1,
    #                       rate=44100,
    #                       input=True,
    #                       frames_per_buffer=1024)


    #     # Open the output microphone stream
    #     output_stream = p.open(format=pyaudio.paInt16,
    #                    channels=1,
    #                    rate=44100,
    #                    output=True)

    #     while True:
    # # Read input microphone data
    #         input_data = input_stream.read(1024)
    # # Perform noise reduction
    #         audio_frame = np.frombuffer(input_data, dtype=np.int16)
    #         reduced_noise = nr.reduce_noise(audio_frame, sr=44100)
    #         audio_data = reduced_noise.tobytes()
    # # Write the audio data to the output microphone stream
    #         output_stream.write(audio_data)

    #     input_stream.stop_stream()
    #     input_stream.close()
    #     output_stream.stop_stream()
    #     output_stream.close()
    #     p.terminate()   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
