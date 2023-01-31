import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import noisereduce as nr
import pyaudio
import numpy as np
import sounddevice as sd

import sounddevice as sd
import numpy as np
import time
import keyboard
import os
from scipy.fft import fft
import matplotlib.pyplot as plt

class App(QWidget):


    test_mic = 0
    #init sound system
    def callback(indata, outdata, frames, time, status):
        if status:
            print(status)
        outdata[:] = indata
    
    stream = sd.Stream(samplerate=44100, blocksize=1024, dtype=np.float32,
                    channels=2, callback=callback)

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
        
        if(App.test_mic==0):
            App.test_mic=1
            print("Mic Start")
            App.stream.start()
        else:
            print("Mic Stop")
            App.test_mic=0
            App.stream.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
