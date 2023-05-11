import sys
import os
# from PySide6 import *
from PyQt5.QtWidgets import QApplication, QMainWindow

import sounddevice as sd
import pyaudio
from threading import Thread
import time

import keyboard
import numpy as np
import noisereduce as nr
from math import sqrt
from pydub import AudioSegment,generators
from scipy.signal import butter, lfilter
import scipy.signal as signal

#Voice Changer
import librosa
import wave

#VC1
swidth = 2
n = 3

# IMPORT GUI FILE
from ui_main import Ui_mainInterface

Noise_reduce_state = False
VC_item_1 = False
VC_item_2 = False
VC_item_3 = False
VC_item_4 = False
Test_mic_state = False
Mute_mic_state = False
Boost_mic_volumeFactor = 1
Pushed_reinit = 0
# UI = Ui_mainInterface()
#update device in main

def Toggle_NoiseReduce():
    global Noise_reduce_state
    if(Noise_reduce_state==False):
        Noise_reduce_state = True
        print("Noise reduce state = ",Noise_reduce_state)
    else:
        Noise_reduce_state = False
        print("Noise reduce state = ",Noise_reduce_state)

def Toggle_TestMic():
    global Test_mic_state
    if(Test_mic_state==False):
        Test_mic_state = True
        print("Microphone test state = ",Test_mic_state)
    else:
        Test_mic_state = False
        print("Microphone test state = ",Test_mic_state)

def Toggle_MuteMic():
    global Mute_mic_state
    if(Mute_mic_state==False):
        Mute_mic_state = True
        print("Microphone mute state = ",Mute_mic_state)
    else:
        Mute_mic_state = False
        print("Microphone mute state = ",Mute_mic_state)

def Boost_Mic(value):
    global Boost_mic_volumeFactor
    if(value == 0):
        value = 1
    Boost_mic_volumeFactor = value/10
    print('Mic factor : ', value/10)
    # Boost_mic_volumeFactor = value/10

#soundpad
# def play_mic(row, filename):
#     fname = filename
#     # convert string to QUrl object using the QUrl constructor
#     print('main', filename)

def VC_item_1_Tog():
    global VC_item_1
    global VC_item_2
    global VC_item_3
    global VC_item_4
    if(VC_item_1==False):
        VC_item_1 = True
        VC_item_2 = False
        VC_item_3 = False
        VC_item_4 = False
        print("VoiceChange_main1 test state = ",VC_item_1)
    else:
        VC_item_1 = False
        print("VoiceChange_main1 test state = ",VC_item_1)

def VC_item_2_Tog():
    global VC_item_1
    global VC_item_2
    global VC_item_3
    global VC_item_4
    if(VC_item_2==False):
        VC_item_1 = False
        VC_item_2 = True
        VC_item_3 = False
        VC_item_4 = False
        print("VoiceChange_main2 test state = ",VC_item_2)
    else:
        VC_item_2 = False
        print("VoiceChange_main2 test state = ",VC_item_2)

def VC_item_3_Tog():
    global VC_item_1
    global VC_item_2
    global VC_item_3
    global VC_item_4
    if(VC_item_3==False):
        VC_item_1 = False
        VC_item_2 = False
        VC_item_3 = True
        VC_item_4 = False
        print("VoiceChange_main3 test state = ",VC_item_3)
    else:
        VC_item_3 = False
        print("VoiceChange_main3 test state = ",VC_item_3)

def VC_item_4_Tog():
    global VC_item_1
    global VC_item_2
    global VC_item_3
    global VC_item_4
    if(VC_item_4==False):
        VC_item_1 = False
        VC_item_2 = False
        VC_item_3 = False
        VC_item_4 = True
        print("VoiceChange_main4 test state = ",VC_item_4)
    else:
        VC_item_4 = False
        print("VoiceChange_main4 test state = ",VC_item_4)

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
            output_sound = audio_data

            #Noise suppression
            if(Noise_reduce_state):
                cutoff_low = 8000
                cutoff_high = 3000
                nyquist_rate = 44100 / 2.0
                pass_order = 5
                pass_stop = 40
                lowpass_coefficients = butter(pass_order, cutoff_low / nyquist_rate, btype='low', analog=False, output='sos')
                highpass_coefficients = butter(pass_order, cutoff_high / nyquist_rate, btype='high', analog=False, output='sos')
                # # print('Noise suppressed')
                audio_frame = np.frombuffer(audio_data, dtype=np.int16)
                audio_frame = signal.decimate(audio_frame, 4, zero_phase=True)
                
                filtered_audio_lowpass = signal.sosfiltfilt(lowpass_coefficients, audio_frame)
                filtered_audio = signal.sosfiltfilt(highpass_coefficients, filtered_audio_lowpass)
                output_sound = filtered_audio.tobytes()
                
                output_sound = nr.reduce_noise(audio_frame, sr=44100)
            # else:
            #     # print('Normal voice')
            #     output_sound = audio_data

            # Boostmic
            self.multiplier = pow(2, (sqrt(sqrt(sqrt(Boost_mic_volumeFactor))) * 192 - 192)/6)
            if(Mute_mic_state):
                sine_segment = generators.Sine(1000).to_audio_segment()
                sine_segment = sine_segment-200
                sine_data = sine_segment.raw_data
                audio_data = sine_data
            else:
                # Boostmic
                self.numpy_data = np.fromstring(audio_data, dtype=np.int16)
                np.multiply(self.numpy_data, self.multiplier, out=self.numpy_data, casting="unsafe")
                audio_data = self.numpy_data.tostring()

            if(VC_item_1):
                data = audio_data
                data = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data))
 
                # do real fast Fourier transform 
                data = np.fft.rfft(data)
                
                # This does the shifting
                data2 = [0]*len(data)
                n = 12
                if n >= 0:
                    data2[n:len(data)] = data[0:(len(data)-n)]
                    data2[0:n] = data[(len(data)-n):len(data)]
                else:
                    data2[0:(len(data)+n)] = data[-n:len(data)]
                    data2[(len(data)+n):len(data)] = data[0:-n]
                
                data = np.array(data2)
                # Done shifting
                
                # inverse transform to get back to temporal data
                data = np.fft.irfft(data)
                
                dataout = np.array(data, dtype='int16') 
                audio_data = wave.struct.pack("%dh"%(len(dataout)), *list(dataout)) #convert back to 16-bit data

            elif(VC_item_2):
                data = audio_data
                data = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data))
 
                # do real fast Fourier transform 
                data = np.fft.rfft(data)
                
                # This does the shifting
                data2 = [0]*len(data)
                n = 3
                if n >= 0:
                    data2[n:len(data)] = data[0:(len(data)-n)]
                    data2[0:n] = data[(len(data)-n):len(data)]
                else:
                    data2[0:(len(data)+n)] = data[-n:len(data)]
                    data2[(len(data)+n):len(data)] = data[0:-n]
                
                data = np.array(data2)
                # Done shifting
                
                # inverse transform to get back to temporal data
                data = np.fft.irfft(data)
                
                dataout = np.array(data, dtype='int16') 
                audio_data = wave.struct.pack("%dh"%(len(dataout)), *list(dataout)) #convert back to 16-bit data

            elif(VC_item_3):
                data = audio_data
                data = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data))
 
                # do real fast Fourier transform 
                data = np.fft.rfft(data)
                
                # This does the shifting
                data2 = [0]*len(data)
                n = -3
                if n >= 0:
                    data2[n:len(data)] = data[0:(len(data)-n)]
                    data2[0:n] = data[(len(data)-n):len(data)]
                else:
                    data2[0:(len(data)+n)] = data[-n:len(data)]
                    data2[(len(data)+n):len(data)] = data[0:-n]
                
                data = np.array(data2)
                # Done shifting
                
                # inverse transform to get back to temporal data
                data = np.fft.irfft(data)
                
                dataout = np.array(data, dtype='int16') 
                audio_data = wave.struct.pack("%dh"%(len(dataout)), *list(dataout)) #convert back to 16-bit data

            elif(VC_item_4):
                data = audio_data
                data = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data))
 
                # do real fast Fourier transform 
                data = np.fft.rfft(data)
                
                # This does the shifting
                data2 = [0]*len(data)
                n = -8
                if n >= 0:
                    data2[n:len(data)] = data[0:(len(data)-n)]
                    data2[0:n] = data[(len(data)-n):len(data)]
                else:
                    data2[0:(len(data)+n)] = data[-n:len(data)]
                    data2[(len(data)+n):len(data)] = data[0:-n]
                
                data = np.array(data2)
                # Done shifting
                
                # inverse transform to get back to temporal data
                data = np.fft.irfft(data)
                
                dataout = np.array(data, dtype='int16') 
                audio_data = wave.struct.pack("%dh"%(len(dataout)), *list(dataout)) #convert back to 16-bit data

            # output_sound = audio_data
            self.virtual_microphone_stream.write(audio_data)

            if(Test_mic_state):
                # print('TesttttttttttttMic')
                self.default_output_stream.write(audio_data)

            #emergency close thread
            # if(keyboard.is_pressed('z')):
            #     break
            # UI.get_audio_data = np.frombuffer(output_sound, dtype=np.int16)
            # UI.audio_from_main()
            # print(UI.get_audio_data)
        #close programclea
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

#voicechanger
    # def Toggle_VC_Item():
    # global Test_item_VC_state
    # if(Test_mic_state==False):
    #     Test_mic_state = True
    #     print("Microphone test state = ",Test_mic_state)
    # else:
    #     Test_mic_state = False
    #     print("Microphone test state = ",Test_mic_state)

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

        # Page Test
        # self.ui.Alert_button.clicked.connect(
        #     lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Alert_page))

        # Page Soundpad
        self.ui.Soundpad_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Soundpad_page))

        # Page Voice Changer
        self.ui.Voicechanger_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Voicechanger_page))
        
        self.ui.pushButton.clicked.connect(self.ui.show_data)
        self.ui.pushButton.clicked.connect(self.ui.update_dashboard_plot)
        self.ui.pushButton.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashbord_page))
        
        # # page settingmain
        self.ui.setting_Button.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6))
        
        # page setting
        self.ui.settingButton.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5))

        #link button
        self.ui.Noise_button.clicked.connect(Toggle_NoiseReduce)
        self.ui.Testmic_button.clicked.connect(Toggle_TestMic)
        self.ui.Voicechange_1.clicked.connect(VC_item_1_Tog)
        self.ui.Voicechange_2.clicked.connect(VC_item_2_Tog)
        self.ui.Voicechange_3.clicked.connect(VC_item_3_Tog)
        self.ui.Voicechange_4.clicked.connect(VC_item_4_Tog)
        self.ui.VC_Testmi_button.clicked.connect(Toggle_TestMic)
        
        
        self.createSound_system = False
        try:
            self.sound_system = SoundSystem()
            print('init successes')
            self.createSound_system = 1

            self.audio_stream = Thread(target = self.sound_system.audio_stream_thread)
            self.audio_stream.daemon = True
            self.audio_stream.start()

            #audio device select
            self.ui.comboBox.currentIndexChanged['QString'].connect(self.sound_system.print_audio_device)
            #microphone device select
            self.ui.comboBox_2.currentIndexChanged['QString'].connect(self.sound_system.print_microphone_device)
            #microphone mute
            self.ui.micmute.clicked.connect(Toggle_MuteMic)
            #boostmic
            self.ui.horizontalSlider_2.valueChanged.connect(Boost_Mic)

            #soundpad
            # self.ui.play_button.clicked.connect(play_mic())

        except:
            print("init in main error")
            print('Please download VB cable or enable VB cable from the setting')
            self.ui.stackedWidget.setCurrentWidget(self.ui.Alert_page)
        
    
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