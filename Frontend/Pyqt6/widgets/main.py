import sys
import os
from PySide6 import *
from PyQt5.QtWidgets import QApplication, QMainWindow

import sounddevice as sd
import pyaudio
from threading import Thread
import time

import keyboard
import numpy as np
import noisereduce as nr

# IMPORT GUI FILE
from ui_main import *

Noise_reduce_state = False
Test_mic_state = False
Pushed_reinit = 0

#update device in main

def Toggle_NoiseReduce():
    global Noise_reduce_state
    if(Noise_reduce_state==False):
        Noise_reduce_state = True
        print("State = ",Noise_reduce_state)
        #ทำstate ปุ่ม
    else:
        Noise_reduce_state = False
        print("State = ",Noise_reduce_state)


def Toggle_TestMic():
    global Test_mic_state
    if(Test_mic_state==0):
        Test_mic_state = 1
        print("State = ",Test_mic_state)
    else:
        Test_mic_state = 0
        print("State = ",Test_mic_state)

def Re_Init_SoundSystem():
    global Pushed_reinit
    Pushed_reinit = 1
    print('try init again')


###
class SoundSystem():
    def __init__(self):
    
        # self.output_sound = ''
        if(self.find_vb()):
            print("Found VB")
        else:
            print("VB not found")
            # print("init error")
            return False

        #init sound system
        self.p = pyaudio.PyAudio()

        #get device info
        # open a stream from microphone
        try:
            self.input_stream = self.p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            input=True,
                            # input_device_index = 3,
                            #   input_device_index=input_device_index,
                            frames_per_buffer=1024)
        except:
            print("Cannot detect microphone")
            return False


        # open a stream for playing audio
        try:
            self.default_output_stream = self.p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            output=True,
                            # output_device_index=output_device_index,
                            frames_per_buffer=1024)
        except:
            print("Cannot detect default output")
            return False

        # open a stream for virtual microphone
        try:
            device_list = sd.query_devices()
            vb_index = self.p.get_default_output_device_info()['index']
            for i in (device_list):
                if "CABLE Input " in i['name']:
                    vb_index = i['index']
                    break
            self.virtual_microphone_stream = self.p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            output=True,
                            frames_per_buffer=1024,
                            output_device_index=vb_index)
        except:
            print("Cannot detect virtual microphone")
            return False

    def find_vb(self):
        device_list = sd.query_devices()
        for i in (device_list):
            if "CABLE Input " in i['name']:
                return True
        print("not found VB")
        return False

    def update_input(self, index):
        try:
            self.input_stream = self.p.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=44100,
                                input=True,
                                input_device_index = index,
                                frames_per_buffer=1024)
            print('update input complete')
        except:
            print('update input err')

    def update_output(self, index):
        try:
            self.default_output_stream = self.p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            output=True,
                            output_device_index = index,
                            frames_per_buffer=1024)
            print('update output complete')
        except:
            print('update input err')

    def audio_stream_thread(self):
        audio_data = self.input_stream.read(1024)
        print("Audio stream start running")
        while len(audio_data) != 0:
            # print('mic stream thread running')
            audio_data = self.input_stream.read(1024)

            #Noise suppression
            if(Noise_reduce_state):
                print('Noise suppressed')
                audio_frame = np.frombuffer(audio_data, dtype=np.int16)
                reduced_noise = nr.reduce_noise(audio_frame, sr=44100)
                output_sound = reduced_noise.tobytes()
            else:
                print('Normal voice')
                output_sound = audio_data
                
            self.virtual_microphone_stream.write(output_sound)

            if(Test_mic_state):
                print('TesttttttttttttMic')
                self.default_output_stream.write(output_sound)

            #emergency close thread
            if(keyboard.is_pressed('z')):
                break

        #close program
        self.input_stream.stop_stream()
        self.input_stream.close()
        self.virtual_microphone_stream.stop_stream()
        self.virtual_microphone_stream.close()
        self.p.terminate()

    def print_audio_device(self, value):
        print('Speaker in main:',value)
        device_list = sd.query_devices()
        for i in (device_list):
            if value[0:30] in i['name'] and i['hostapi'] == 0:
                print(i['index'])
                self.update_output(i['index'])
                break
    
    def print_microphone_device(self, value):
        print('Microphone in main:',value)
        device_list = sd.query_devices()
        for i in (device_list):
            if value[0:30] in i['name'] and i['hostapi'] == 0:
                print(i['index'])
                self.update_input(i['index'])
                break
###

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_mainInterface()
        self.ui.setupUi(self)

        #Page links33
        ########################################################################################
        # Page Microphone
        self.ui.Microphone_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Microphone_page))

        # Page Audio
        self.ui.Audio_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Audio_page))

        # Page Soundpad
        self.ui.Soundpad_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Soundpad_page))

        # Page Voice Changer
        self.ui.Voicechanger_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Voicechanger_page))

        #link button
        self.ui.Noise_button.clicked.connect(Toggle_NoiseReduce)
        self.ui.Testmic_button.clicked.connect(Toggle_TestMic)
        
        self.createSound_system = False
        try:
            self.sound_system = SoundSystem()
            print('init successes')
            self.createSound_system = 1

            self.audio_stream = Thread(target = self.sound_system.audio_stream_thread)
            self.audio_stream.daemon = True
            self.audio_stream.start()

            #audio
            self.ui.comboBox.currentIndexChanged['QString'].connect(self.sound_system.print_audio_device)
            #microphone
            self.ui.comboBox_2.currentIndexChanged['QString'].connect(self.sound_system.print_microphone_device)

        except:
            print("init in main error")
            print('Please download VB cable or enable VB cable from the setting')
            self.ui.stackedWidget.setCurrentWidget(self.ui.Audio_page)


        # while(self.createSound_system == False):
        #     #nav to Error handler page
        #     print('error')

        # while(self.create == 0):
        #     global Pushed_reinit
        #     if(Pushed_reinit == 1):
        #         Pushed_reinit = 0
        #         try:
        #             self.sound_system = SoundSystem()
        #             create = 1
        #         except:
        #             print("init in main error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    nextGui = MainWindow()
    nextGui.show()
    sys.exit(app.exec_())

#thread.ident != None and thread.is_alive() == False