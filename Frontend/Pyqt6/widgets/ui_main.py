import os
import pickle
import time
import subprocess

# from icons import icons_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizePolicy, QHeaderView, QAbstractItemView, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioDeviceInfo, QAudio

from mutagen.mp3 import MP3
from mutagen.wave import WAVE

import pyaudio
import sounddevice as sd
import wave
import threading

# IMPORT GUI FILE
# from pages.soundpad_page import *
# from PySide6 import QtMultimedia
from PyQt5 import uic
# import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import keyboard

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import queue
import sys
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import pyaudio
from scipy.signal import butter, lfilter
import scipy.signal as signal
# import graph file

# from newgraph import MicrophoneAudioWaveform
input_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioInput)
output_audio_deviceInfos = QAudioDeviceInfo.availableDevices(
    QAudio.AudioOutput)


try:
    p = pyaudio.PyAudio()
    device_list = sd.query_devices()
    vb_index = p.get_default_output_device_info()['index']
    for i in (device_list):
        if "CABLE Input " in i['name']:
            vb_index = i['index']
            break
    ui_virtual_microphone_stream = p.open(format=pyaudio.paInt16,
                                          channels=1,
                                          rate=44100,
                                          output=True,
                                          frames_per_buffer=1024,
                                          output_device_index=vb_index)
except:
    print("Cannot detect virtual microphone _ ui")

micplay = False
micplay_file = "none"
stop_threads = False


class Ui_mainInterface(object):
    noise_reduce = 0
    test_microphone = 0
    VC_test_microphone = 0
    VC_item_1 = 0
    VC_item_2 = 0
    VC_item_3 = 0
    VC_item_4 = 0
    microphone_mute = 0
    audio_mute = 0
    Mic_Side_menu = 0
    SP_Side_menu = 0
    VC_Side_menu = 0

    def __init__(self):
        self.get_audio_data = np.zeros(1024)
        self.q = queue.Queue()
        self.q_normal = queue.Queue()
        self.q_reduce = queue.Queue()
        self.current_plot = 'normal'

    def setupUi(self, ui_main):
        # Application size
        ui_main.setObjectName("ui_main")
        ui_main.setEnabled(True)
        ui_main.resize(1280, 720)
        ui_main.setMinimumSize(QtCore.QSize(1280, 720))
        ui_main.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        ui_main.setFont(font)
        ui_main.setMouseTracking(False)
        ui_main.setAutoFillBackground(False)
        ui_main.setStyleSheet("*{\n"
                              "    border:none;\n"
                              "    background-color: transparent;\n"
                              "}\n"
                              "#centralrwidget{\n"
                              "    background-color: #040f13;\n"
                              "}\n"
                              "#side_menu{\n"
                              "    background-color: #071e26;\n"
                              "    border-radius: 20px;\n"
                              "}\n"
                              "#QPushButton{\n"
                              "    padding: 10px;\n"
                              "    background-color: #040f13;\n"
                              "    border-radius: 5px;\n"
                              "}\n"
                              "#main_body{\n"
                              "    background-color: #071e26;\n"
                              "    border-radius: 10px;\n"
                              "}")
        # LEFT SIDE
        self.Left_side = QtWidgets.QFrame(ui_main)
        self.Left_side.setGeometry(QtCore.QRect(-1, 0, 380, 721))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Left_side.sizePolicy().hasHeightForWidth())
        self.Left_side.setSizePolicy(sizePolicy)
        self.Left_side.setMinimumSize(QtCore.QSize(380, 700))
        self.Left_side.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Left_side.setStyleSheet("QFrame{\n"
                                     "    \n"
                                     "    background-color: rgb(50, 75, 79);\n"
                                     "}")
        self.Left_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Left_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Left_side.setObjectName("Left_side")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.Left_side)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0, 381, 721))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_2 = QtWidgets.QFrame(self.page_5)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 381, 321))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        # MENUBARS
        self.Menubars = QtWidgets.QWidget(self.frame_2)
        self.Menubars.setGeometry(QtCore.QRect(-1, -1, 381, 330))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Menubars.sizePolicy().hasHeightForWidth())
        self.Menubars.setSizePolicy(sizePolicy)
        self.Menubars.setMinimumSize(QtCore.QSize(360, 330))
        self.Menubars.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Menubars.setObjectName("Menubars")

        # menu button
        self.Menu_button = QtWidgets.QFrame(self.Menubars)
        self.Menu_button.setGeometry(QtCore.QRect(-1, 19, 381, 306))
        self.Menu_button.setStyleSheet("QPushButton{\n"
                                       "    text-align: left;\n"
                                       "    padding-left: 20 px;\n"
                                       "    color: #FFFFFF;\n"
                                       "}")

        self.Menu_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu_button.setObjectName("Menu_button")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Menu_button)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Microphone button
        self.Microphone_button = QtWidgets.QPushButton(self.Menu_button)
        self.Microphone_button.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        self.Microphone_button.setFont(font)
        self.Microphone_button.setStyleSheet("QPushButton{\n"
                                             "    background-color: rgba(0, 0, 0, 0)\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                             "}"
                                             )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/mic8.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Microphone button clicked
        self.Microphone_button.clicked.connect(self.Mic_Side_menu_clicked)

        self.Microphone_button.setIcon(icon)
        self.Microphone_button.setIconSize(QtCore.QSize(40, 40))
        self.Microphone_button.setObjectName("Microphone_button")
        self.verticalLayout.addWidget(self.Microphone_button)

        # Alert button
        # self.Alert_button = QtWidgets.QPushButton(self.Menu_button)
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI")
        # font.setPointSize(28)
        # self.Alert_button.setFont(font)
        # self.Alert_button.setStyleSheet("QPushButton{\n"
        #                                 "    background-color: rgba(0, 0, 0, 0)\n"
        #                                 "}\n"
        #                                 "QPushButton:hover{\n"
        #                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
        #                                 "}"
        #                                 )

        # self.Alert_button.setIconSize(QtCore.QSize(40, 40))
        # self.Alert_button.setObjectName("Alert_button")
        # self.verticalLayout.addWidget(self.Alert_button)

        # Soundpad button
        self.Soundpad_button = QtWidgets.QPushButton(self.Menu_button)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        self.Soundpad_button.setFont(font)
        self.Soundpad_button.setStyleSheet("QPushButton{\n"
                                           "    background-color: rgba(0, 0, 0, 0)\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                           "}"
                                           )
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/play-circle8.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Soundpad button clicked
        self.Soundpad_button.clicked.connect(self.SP_Side_menu_clicked)

        self.Soundpad_button.setIcon(icon2)
        self.Soundpad_button.setIconSize(QtCore.QSize(40, 40))
        self.Soundpad_button.setObjectName("Soundpad_button")
        self.verticalLayout.addWidget(self.Soundpad_button)
        self.Voicechanger_button = QtWidgets.QPushButton(self.Menu_button)

        # Voicechanger button
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        self.Voicechanger_button.setFont(font)
        self.Voicechanger_button.setStyleSheet("QPushButton{\n"
                                               "    background-color: rgba(0, 0, 0, 0)\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                               "}"
                                               )
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/code-sandbox8.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Voicechanger button clicked
        self.Voicechanger_button.clicked.connect(self.VC_Side_menu_clicked)

        self.Voicechanger_button.setIcon(icon3)
        self.Voicechanger_button.setIconSize(QtCore.QSize(40, 40))
        self.Voicechanger_button.setObjectName("Voicechanger_button")
        self.verticalLayout.addWidget(self.Voicechanger_button)
        self.frame_3 = QtWidgets.QFrame(self.page_5)
        self.frame_3.setGeometry(QtCore.QRect(0, 330, 381, 381))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Device_settings = QtWidgets.QFrame(self.frame_3)
        self.Device_settings.setGeometry(QtCore.QRect(0, -10, 372, 391))
        # self.Device_settings = QtWidgets.QFrame(self.Left_side)

        # Device settings
        # self.Device_settings.setGeometry(QtCore.QRect(0, 330, 372, 391))

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Device_settings.sizePolicy().hasHeightForWidth())
        self.Device_settings.setSizePolicy(sizePolicy)
        self.Device_settings.setMinimumSize(QtCore.QSize(360, 330))
        self.Device_settings.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Device_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Device_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Device_settings.setObjectName("Device_settings")

# Setting Zone
###################################################################################
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Device_settings)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dropdownslider1 = QtWidgets.QFrame(self.Device_settings)
        self.dropdownslider1.setMinimumSize(QtCore.QSize(370, 0))
        self.dropdownslider1.setStyleSheet("")
        self.dropdownslider1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropdownslider1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropdownslider1.setObjectName("dropdownslider1")
        self.comboBox_2 = QtWidgets.QComboBox(self.dropdownslider1)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 50, 273, 44))
        self.comboBox_2.setMinimumSize(QtCore.QSize(273, 44))
        self.comboBox_2.setMaximumSize(QtCore.QSize(273, 44))
        self.comboBox_2.setStyleSheet("QComboBox{\n"
                                      "background-color: rgb(26, 39, 41);\n"
                                      "border-radius: 8px;\n"
                                      "border: 5px solid rgb(26, 39, 41);\n"
                                      "color: white;\n"
                                      "font-size: 13px;\n"
                                      "}\n"
                                      "QComboBox:editable {\n"
                                      "background-color: #324B4F;\n"
                                      "}\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "border: 1px solid #d9d9d9;\n"
                                      "selection-background-color: #686868;\n"
                                      "border-bottom-right-radius: 8px;\n"
                                      "border-bottom-left-radius: 8px;\n"
                                      "background-color: #d9d9d9;\n"
                                      "color: #686868;\n"
                                      "font-size: 13px;\n"
                                      "}\n"
                                      "")
        self.comboBox_2.setObjectName("comboBox_2")
        self.micmute = QtWidgets.QPushButton(self.dropdownslider1)
        self.micmute.setGeometry(QtCore.QRect(20, 50, 45, 45))
        self.micmute.setMinimumSize(QtCore.QSize(45, 45))
        self.micmute.setMaximumSize(QtCore.QSize(45, 45))
        self.micmute.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/mic-sai8.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.micmute.setIcon(icon4)
        self.micmute.setIconSize(QtCore.QSize(40, 40))
        self.micmute.setObjectName("micmute")

        # เรียกใช้ฟังก์ชั่น mute mic
        self.micmute.clicked.connect(self.mic_mute)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.dropdownslider1)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(30, 110, 326, 20))
        self.horizontalSlider_2.setStyleSheet("QSlider::handle:horizontal {\n"
                                              "border-radius: 6px;\n"
                                              "background-color: #00d19d;;\n"
                                              "}")

        # กำหนดค่า max min ค่ากลาง ของ Boost mic
        self.horizontalSlider_2.setMaximum(20)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setValue(10)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.valueChanged.connect(self.updateboostmicl)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_2.addWidget(self.dropdownslider1)
        self.dropdownslider2 = QtWidgets.QFrame(self.Device_settings)
        self.dropdownslider2.setMinimumSize(QtCore.QSize(370, 0))
        self.dropdownslider2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropdownslider2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropdownslider2.setObjectName("dropdownslider2")
        self.comboBox = QtWidgets.QComboBox(self.dropdownslider2)
        self.comboBox.setGeometry(QtCore.QRect(80, 40, 273, 44))
        self.comboBox.setMinimumSize(QtCore.QSize(273, 44))
        self.comboBox.setMaximumSize(QtCore.QSize(273, 44))
        self.comboBox.setStyleSheet("QComboBox{\n"
                                    "background-color: rgb(26, 39, 41);\n"
                                    "border-radius: 8px;\n"
                                    "border: 5px solid rgb(26, 39, 41);\n"
                                    "color: white;\n"
                                    "font-size: 13px;\n"
                                    "}\n"
                                    "QComboBox:editable {\n"
                                    "background-color: #324B4F;\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "border: 1px solid #d9d9d9;\n"
                                    "selection-background-color: #686868;\n"
                                    "border-bottom-right-radius: 8px;\n"
                                    "border-bottom-left-radius: 8px;\n"
                                    "background-color: #d9d9d9;\n"
                                    "color: #686868;\n"
                                    "font-size: 13px;\n"
                                    "}\n"
                                    "")
        self.comboBox.setObjectName("comboBox")

        # เอา Virtual Cable ออกจาก List
        # โชว์ข้อมูล Input ใน dropdown

        self.devicesInput_list = []
        for device in input_audio_deviceInfos:
            if device.deviceName() not in self.devicesInput_list and "Virtual Cable" not in device.deviceName():
                self.devicesInput_list.append(device.deviceName())

        self.comboBox_2.addItems(self.devicesInput_list)
        self.comboBox_2.currentIndexChanged['QString'].connect(
            self.updateInput_now)
        self.comboBox_2.setCurrentIndex(0)

        # โชว์ข้อมูล Output ใน dropdown
        self.devicesOutput_list = []
        for device in output_audio_deviceInfos:
            if device.deviceName() not in self.devicesOutput_list and "Virtual Cable" not in device.deviceName():
                self.devicesOutput_list.append(device.deviceName())

        self.comboBox.addItems(self.devicesOutput_list)
        self.comboBox.currentIndexChanged['QString'].connect(
            self.updateOutput_now)
        self.comboBox.setCurrentIndex(0)

        ##################
        self.speakermute = QtWidgets.QPushButton(self.dropdownslider2)
        self.speakermute.setGeometry(QtCore.QRect(20, 40, 45, 45))
        self.speakermute.setMinimumSize(QtCore.QSize(45, 45))
        self.speakermute.setMaximumSize(QtCore.QSize(45, 45))
        self.speakermute.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/unmutespeaker-sai8.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speakermute.setIcon(icon5)
        self.speakermute.setIconSize(QtCore.QSize(40, 40))
        self.speakermute.setObjectName("speakermute")
        # เรียกใช้ ฟังก์ชั่น mute volume
        self.speakermute.clicked.connect(self.volume_mute)

        self.horizontalSlider = QtWidgets.QSlider(self.dropdownslider2)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 100, 326, 20))
        self.horizontalSlider.setStyleSheet("QSlider::handle:horizontal {\n"
                                            "border-radius: 6px;\n"
                                            "background-color: #00d19d;;\n"
                                            "}")
        # set ให้ค่า current เท่ากับ value
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        current_percent = current * 100
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setMinimum(0)

        # set ให้โชว์ค่า value ตรง Slider bar
        self.horizontalSlider.setValue(int(current_percent))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.updatevolume)
        self.volume = self.get_volume()
        self.verticalLayout_2.addWidget(self.dropdownslider2)
        self.frame = QtWidgets.QFrame(self.Device_settings)
        self.frame.setMinimumSize(QtCore.QSize(370, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.setting_Button = QtWidgets.QPushButton(self.frame)
        self.setting_Button.setGeometry(QtCore.QRect(30, 59, 320, 70))
        self.setting_Button.setMinimumSize(QtCore.QSize(320, 70))
        self.setting_Button.setMaximumSize(QtCore.QSize(320, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.setting_Button.setFont(font)
        self.setting_Button.setStyleSheet("QPushButton \n"
                                          "{\n"
                                          " color: #FFFFFF;\n"
                                          "}")

        # # เรียกใช้ ฟังก์ชั่น open_setting
        # self.setting_Button.clicked.connect(self.open_setting)

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/setting8.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.setting_Button.setIcon(icon6)
        self.setting_Button.setIconSize(QtCore.QSize(40, 40))
        self.setting_Button.setObjectName("setting_Button")
        self.verticalLayout_2.addWidget(self.frame)
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frameSetting = QtWidgets.QFrame(self.page_6)
        self.frameSetting.setGeometry(QtCore.QRect(0, 0, 371, 101))
        self.frameSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSetting.setObjectName("frameSetting")
        self.settingmain = QtWidgets.QPushButton(self.frameSetting)
        self.settingmain.setGeometry(QtCore.QRect(20, 20, 320, 70))
        self.settingmain.setMinimumSize(QtCore.QSize(320, 70))
        self.settingmain.setMaximumSize(QtCore.QSize(320, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.settingmain.setFont(font)
        self.settingmain.setStyleSheet("QPushButton { \n"
                                       "    color: #ffffff;\n"
                                       "}")
        self.settingmain.setIconSize(QtCore.QSize(32, 32))
        self.settingmain.setObjectName("settingmain")
        self.framedefault = QtWidgets.QFrame(self.page_6)
        self.framedefault.setGeometry(QtCore.QRect(0, 100, 371, 180))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.framedefault.sizePolicy().hasHeightForWidth())
        self.framedefault.setSizePolicy(sizePolicy)
        self.framedefault.setMinimumSize(QtCore.QSize(0, 180))
        self.framedefault.setMaximumSize(QtCore.QSize(16777215, 180))
        self.framedefault.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framedefault.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framedefault.setObjectName("framedefault")
        self.detaildefault = QtWidgets.QTextEdit(self.framedefault)
        self.detaildefault.setGeometry(QtCore.QRect(30, 20, 321, 121))
        self.detaildefault.setObjectName("detaildefault")

        self.frameEquipment = QtWidgets.QFrame(self.page_6)
        self.frameEquipment.setGeometry(QtCore.QRect(0, 280, 371, 191))
        self.frameEquipment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEquipment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEquipment.setObjectName("frameEquipment")
        self.detailequipment = QtWidgets.QTextEdit(self.frameEquipment)
        self.detailequipment.setGeometry(QtCore.QRect(30, 10, 321, 61))
        self.detailequipment.setObjectName("detailequipment")
        self.Equipmentsetting = QtWidgets.QPushButton(self.frameEquipment)
        self.Equipmentsetting.clicked.connect(self.open_device)
        self.Equipmentsetting.setGeometry(QtCore.QRect(30, 80, 320, 54))
        self.Equipmentsetting.setMinimumSize(QtCore.QSize(320, 54))
        self.Equipmentsetting.setMaximumSize(QtCore.QSize(320, 54))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.Equipmentsetting.setFont(font)
        self.Equipmentsetting.setStyleSheet("QPushButton { \n"
                                            "    background-color: #850021;\n"
                                            "    color: #ffffff;\n"
                                            "}")
        self.Equipmentsetting.setObjectName("Equipmentsetting")
        # self.Equipmentsetting.connect(self.open_device)
        self.frametutorial = QtWidgets.QFrame(self.page_6)
        self.frametutorial.setGeometry(QtCore.QRect(0, 470, 371, 121))
        self.frametutorial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frametutorial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frametutorial.setObjectName("frametutorial")
        self.Tutorial = QtWidgets.QPushButton(self.frametutorial)
        self.Tutorial.setGeometry(QtCore.QRect(30, 50, 320, 54))
        self.Tutorial.setMinimumSize(QtCore.QSize(320, 54))
        self.Tutorial.setMaximumSize(QtCore.QSize(320, 54))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.Tutorial.setFont(font)
        self.Tutorial.setStyleSheet("QPushButton { \n"
                                    "    background-color: #56B7C7;\n"
                                    "    color: #ffffff;\n"
                                    "}")
        self.Tutorial.setObjectName("Tutorial")
        self.frame_8 = QtWidgets.QFrame(self.page_6)
        self.frame_8.setGeometry(QtCore.QRect(0, 590, 372, 130))
        self.frame_8.setMinimumSize(QtCore.QSize(370, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.settingButton = QtWidgets.QPushButton(self.frame_8)
        self.settingButton.setGeometry(QtCore.QRect(30, 50, 320, 70))
        self.settingButton.setMinimumSize(QtCore.QSize(320, 70))
        self.settingButton.setMaximumSize(QtCore.QSize(320, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.settingButton.setFont(font)
        self.settingButton.setStyleSheet("QPushButton { \n"
                                         "    color: #ffffff;\n"
                                         "}")

        # self.settingButton.setIcon(icon6)
        self.settingButton.setIconSize(QtCore.QSize(32, 32))
        self.settingButton.setObjectName("settingButton")
        self.stackedWidget_2.addWidget(self.page_6)

        # right side
        self.Right_side = QtWidgets.QFrame(ui_main)
        self.Right_side.setGeometry(QtCore.QRect(380, 0, 900, 720))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Right_side.sizePolicy().hasHeightForWidth())
        self.Right_side.setSizePolicy(sizePolicy)
        self.Right_side.setMinimumSize(QtCore.QSize(900, 700))
        self.Right_side.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setKerning(True)
        self.Right_side.setFont(font)
        self.Right_side.setStyleSheet("QFrame{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0.506091, y1:0, x2:0.506, y2:1, stop:0 rgba(74, 111, 117, 255), stop:1 rgba(98, 148, 156, 255));\n"
                                      "}")

        self.Right_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Right_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Right_side.setObjectName("Right_side")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Right_side)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # stacked widget
        # set stacked widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.Right_side)
        self.stackedWidget.setMinimumSize(QtCore.QSize(900, 720))
        self.stackedWidget.setMaximumSize(QtCore.QSize(900, 720))
        self.stackedWidget.setObjectName("stackedWidget")

        # Microphone page size
        self.Microphone_page = QtWidgets.QWidget()
        self.Microphone_page.setMinimumSize(QtCore.QSize(900, 720))
        self.Microphone_page.setMaximumSize(QtCore.QSize(900, 720))
        self.Microphone_page.setObjectName("Microphone_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Microphone_page)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.Microphone_page)
        self.frame.setMinimumSize(QtCore.QSize(900, 720))
        self.frame.setMaximumSize(QtCore.QSize(900, 720))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # frame layout
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Mic title
        self.Mic_title = QtWidgets.QFrame(self.frame)
        self.Mic_title.setMinimumSize(QtCore.QSize(900, 120))
        self.Mic_title.setMaximumSize(QtCore.QSize(900, 120))
        self.Mic_title.setStyleSheet("QFrame{\n"
                                     "    background-color: rgba(0, 0, 0, 0);\n"
                                     "}")
        self.Mic_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mic_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mic_title.setObjectName("Mic_title")

        # Mic title layout
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Mic_title)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Mic_title_label = QtWidgets.QLabel(self.Mic_title)
        self.Mic_title_label.setMinimumSize(QtCore.QSize(900, 120))
        self.Mic_title_label.setMaximumSize(QtCore.QSize(900, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.Mic_title_label.setFont(font)
        self.Mic_title_label.setStyleSheet("QLabel \n"
                                           "{\n"
                                           " color: #FFFFFF;\n"
                                           "}")
        self.Mic_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Mic_title_label.setObjectName("Mic_title_label")
        self.verticalLayout_4.addWidget(self.Mic_title_label)
        self.verticalLayout_2.addWidget(self.Mic_title)

        # Mic settings
        self.Noise = QtWidgets.QFrame(self.frame)
        self.Noise.setMinimumSize(QtCore.QSize(900, 200))
        self.Noise.setMaximumSize(QtCore.QSize(900, 200))
        self.Noise.setStyleSheet("QFrame{\n"
                                 "    background-color: rgba(0, 0, 0, 0);\n"
                                 "}")
        self.Noise.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Noise.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Noise.setObjectName("Noise")

        # noise button
        self.Noise_button = QtWidgets.QPushButton(self.Noise)
        self.Noise_button.setGeometry(QtCore.QRect(50, 10, 780, 180))
        self.Noise_button.setMinimumSize(QtCore.QSize(780, 180))
        self.Noise_button.setMaximumSize(QtCore.QSize(780, 180))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.Noise_button.setFont(font)
        self.Noise_button.setStyleSheet("QPushButton{\n"
                                        "    background-color: #244D54;\n"
                                        "    border-style : outset;\n"
                                        "    border-width : 0.5px;\n"
                                        "    border-radius: 40px;\n"
                                        "    border-color : black;\n"
                                        "\n"
                                        "    color: #686868;\n"
                                        "    text-align : center;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(53, 112, 122);    \n"
                                        "    border-width : 0.5px;\n"
                                        "    border-color :  rgb(1, 209, 158) ;\n"
                                        "    color: #B0B0B0;\n"
                                        "}")
        self.Noise_button.setObjectName("Noise_button")

        # Noice button Function
        self.Noise_button.clicked.connect(self.Noise_button_clicked)

        self.Noise_label = QtWidgets.QLabel(self.Noise)
        self.Noise_label.setGeometry(QtCore.QRect(280, 16, 340, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.Noise_label.setFont(font)
        self.Noise_label.setStyleSheet("QLabel {\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                                       "\n"
                                       "    color: rgb(204, 204, 204);\n"
                                       "}")
        self.Noise_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Noise_label.setObjectName("Noise_label")
        self.verticalLayout_2.addWidget(self.Noise)

        self.Graph = QtWidgets.QFrame(self.frame)
        self.Graph.setStyleSheet("QFrame{\n"
                                 "    background-color: rgba(0, 0, 0, 0);\n"
                                 "}")
        self.Graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph.setObjectName("Graph")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Graph)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #######################################################################
        # Audio parameters
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK_SIZE = 1024
        # self.CALLBACK = self.normal_audio_callback
        self.PLOT = self.normal_update_plot

        # Plot parameters
        self.WINDOW_SIZE = 1000  # ms
        self.DOWN_SAMPLE = 1
        self.CHANNELS_TO_PLOT = [0]

        # Initialize queue for incoming audio data
        # self.q = queue.Queue()

        # Calculate number of samples to display in window
        self.window_samples = int(
            self.WINDOW_SIZE * self.RATE / 1000 / self.DOWN_SAMPLE)

        # Initialize plot data
        self.plot_data = np.zeros(
            (self.window_samples, len(self.CHANNELS_TO_PLOT)))

        # init plot
        self.figure = Figure()
        # self.rect = plt.Rectangle((0.0017, 0.002), 0.995, 0.999, fill=False,
        #                           lw=1, zorder=1000, transform=self.figure.transFigure, figure=self.figure)
        # self.figure.patches.extend([self.rect])
        self.figure.patch.set_facecolor('none')
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # init lines
        # self.lines = self.ax.plot(self.plot_data, color=(0, 1, 0.29))
        self.lines = self.ax.plot(self.plot_data, color=(0, 0, 0))

        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,
                                   frames_per_buffer=self.CHUNK_SIZE, stream_callback=self.normal_audio_callback)

        # self.audio_from_main()

        self.ax.set_facecolor((0, 0, 0))
        self.ax.set_yticks([0])
        self.ax.yaxis.grid(True)
        self.ax.set_ylim(-0.3, 0.3)
        # self.ani = FuncAnimation(self.figure, self.normal_update_plot, interval=30, blit=True)
        self.timer = QTimer()
        # self.timer.stop()
        # self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.PLOT)
        self.timer.start(30)

        plt.show()
        self.verticalLayout_3.addWidget(self.canvas)
        self.verticalLayout_2.addWidget(self.Graph)

        # Test Mic layout
        self.TestMic = QtWidgets.QFrame(self.frame)
        self.TestMic.setMinimumSize(QtCore.QSize(900, 120))
        self.TestMic.setMaximumSize(QtCore.QSize(900, 120))
        self.TestMic.setStyleSheet("QFrame{\n"
                                   "    background-color: rgba(0, 0, 0, 0);\n"
                                   "\n"
                                   "    padding-left: 38px;\n"
                                   "    padding-top: 0px;\n"
                                   "    padding-bottom: 20px;\n"
                                   "}")
        self.TestMic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TestMic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TestMic.setObjectName("TestMic")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.TestMic)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # Test Mic Button
        self.Testmic_button = QtWidgets.QPushButton(self.TestMic)
        self.Testmic_button.setMinimumSize(QtCore.QSize(780, 80))
        self.Testmic_button.setMaximumSize(QtCore.QSize(780, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.Testmic_button.setFont(font)
        self.Testmic_button.setStyleSheet("QPushButton{\n"
                                          "    background-color: #244D54;\n"
                                          "    border-style : outset;\n"
                                          "    border-width : 0.5px;\n"
                                          "    border-radius: 25px;\n"
                                          "    border-color : black;\n"
                                          "\n"
                                          "    color: #686868;\n"
                                          "    text-align : center;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #35707A;    \n"
                                          "    border-width : 0.5px;\n"
                                          "    border-color :  rgb(1, 209, 158) ;\n"
                                          "    color: rgb(204, 204, 204);\n"
                                          "}\n"
                                          )
        self.Testmic_button.setObjectName("Testmic_button")

        # Test Mic Button Function
        self.Testmic_button.clicked.connect(self.TestMic_button_clicked)

        self.verticalLayout_5.addWidget(self.Testmic_button)
        self.verticalLayout_2.addWidget(self.TestMic)
        self.horizontalLayout_2.addWidget(self.frame)
        self.stackedWidget.addWidget(self.Microphone_page)

        # Alert Page
        self.Alert_page = QtWidgets.QWidget()
        self.Alert_page.setObjectName("Alert_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Alert_page)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Alert_Frame = QtWidgets.QFrame(self.Alert_page)
        self.Alert_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Alert_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Alert_Frame.setObjectName("Alert_Frame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.Alert_Frame)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_4 = QtWidgets.QFrame(self.Alert_Frame)
        self.frame_4.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Alert_icon = QtWidgets.QPushButton(self.frame_4)
        self.verticalLayout_10.setContentsMargins(300, 100, 50, 0)
        self.verticalLayout_10.setSpacing(0)
        self.Alert_icon.setMinimumSize(QtCore.QSize(300, 300))
        self.Alert_icon.setMaximumSize(QtCore.QSize(300, 300))
        self.Alert_icon.setObjectName("Alert_icon")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/alert.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Alert_icon.setIcon(icon)
        self.Alert_icon.setIconSize(QtCore.QSize(250, 250))
        self.verticalLayout_10.addWidget(self.Alert_icon)
        self.verticalLayout_19.addWidget(self.frame_4)
        self.Text_Frame = QtWidgets.QFrame(self.Alert_Frame)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.Text_Frame.setFont(font)
        self.Text_Frame.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                      "color:#ffffff\n"
                                      "")
        self.Text_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Text_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Text_Frame.setObjectName("Text_Frame")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.Text_Frame)
        self.verticalLayout_20.setContentsMargins(50, 0, 50, 250)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label = QtWidgets.QLabel(self.Text_Frame)
        self.label.setObjectName("label")
        self.verticalLayout_20.addWidget(self.label)
        self.Alert_button_detail = QtWidgets.QPushButton(self.Text_Frame)

        self.Alert_button_detail.clicked.connect(
            self.Alert_button_detail_clicked)

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.Alert_button_detail.setFont(font)
        self.Alert_button_detail.setStyleSheet("")
        self.Alert_button_detail.setObjectName("Alert_button_detail")
        self.verticalLayout_20.addWidget(self.Alert_button_detail)
        self.verticalLayout_19.addWidget(self.Text_Frame)
        self.horizontalLayout_3.addWidget(self.Alert_Frame)
        self.stackedWidget.addWidget(self.Alert_page)

        # Dashbord Page
        self.dashbord_page = QtWidgets.QWidget()
        self.dashbord_page.setObjectName("dashbord")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.dashbord_page)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # self.dashbord_label = QtWidgets.QLabel(self.Audio_page)
        self.frame_dash_page = QtWidgets.QFrame(self.dashbord_page)
        self.frame_dash_page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dash_page.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dash_page.setObjectName("frame_dash_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_dash_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_dash_title = QtWidgets.QFrame(self.frame_dash_page)
        self.frame_dash_title.setMinimumSize(QtCore.QSize(900, 120))
        self.frame_dash_title.setMaximumSize(QtCore.QSize(900, 120))
        self.frame_dash_title.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.frame_dash_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dash_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dash_title.setObjectName("frame_dash_title")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_dash_title)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.dash_label = QtWidgets.QLabel(self.frame_dash_title)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        # self.dashbord_label.setFont(font)
        # self.dashbord_label.setStyleSheet("color: #66DAED")
        # self.dashbord_label.setAlignment(QtCore.Qt.AlignCenter)
        # self.dashbord_label.setObjectName("dashbord_label")
        # self.horizontalLayout_6.addWidget(self.dashbord_label)
        self.dash_label.setFont(font)
        self.dash_label.setStyleSheet("QLabel \n"
"{\n"
" color: #FFFFFF;\n"
"}")
        self.dash_label.setObjectName("dash_label")
        self.verticalLayout_11.addWidget(self.dash_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.frame_dash_title)
        self.frame_7 = QtWidgets.QFrame(self.frame_dash_page)
        self.frame_7.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setMinimumSize(QtCore.QSize(900, 150))
        self.frame_9.setMaximumSize(QtCore.QSize(900, 150))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        # frame_9 ใส่อันดับ
        # self.text_edit = QtWidgets.QTextEdit(self.frame_9)
        # self.text_edit.setGeometry(QtCore.QRect(10, 10, 880, 130))
        # self.text_edit.setObjectName("text_edit")
        # self.text_edit.setReadOnly(True)

        self.label_dash = QtWidgets.QLabel(self.frame_9)
        self.label_dash.setGeometry(QtCore.QRect(10, 10, 880, 130))
        self.label_dash.setObjectName("label_dash")

        self.verticalLayout_d = QtWidgets.QVBoxLayout(self.frame_9)
        # self.verticalLayout_d.addWidget(self.text_edit)
        self.verticalLayout_d.addWidget(self.label_dash)

        self.show_data()

        # self.text_edit.setStyleSheet("background-color: rgba(0, 0, 0, 0.3);color: #fff; font-size: 21px;border: 3px solid #52ffff;border-radius: 10px; padding-left:15px; padding-top: 16px;")
        
        self.verticalLayout_12.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_2 = QtWidgets.QWidget(self.frame_10)
        self.widget_2.setObjectName("widget_2")

        # self.fig = Figure()
        # self.ax_d = self.fig.add_subplot(111)
        # # fig, ax = plt.subplots()
        # # ax.axis('equal')

        # # อ่านไฟล์ sort_counts.txt เพื่อใช้ในการสร้างกราฟ
        # file_path = 'sort_counts.txt'
        # with open(file_path, 'r') as f:
        #     lines = f.readlines()

        # data = {}
        # texts = []
        # for line in lines:
        #     line = line.strip()
        #     parts = line.split(',')
        #     text = parts[0]
        #     number = int(parts[1])
        #     data[text] = number
        # colors = ['#B9DDF1', '#9FCAE6', '#73A4CA', '#497AA7', '#244D54', '#999999', '#C9C9C9', '#F8B195', '#F67280', '#C06C84']
        # explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)    
        # labels = list(data.keys())[:10]
        # values = list(data.values())[:10]
        
        # self.canvas_d = FigureCanvas()
        self.fig = Figure()
        self.ax_d = self.fig.add_subplot(111)
        self.canvas_d = FigureCanvas(self.fig)
        # layout = QtWidgets.QVBoxLayout(self.widget_2)
        # layout.addWidget(self.canvas_d) 
        # self.ax = self.canvas_d.figure.subplots()
        # self.pie = None

        self.update_dashboard_plot()

        # self.update_dashboard_plot()

        # # create the pie plot
        # wedges, texts, autotexts = ax.pie(self.values, colors=self.colors, labels=self.labels,
        #                                 autopct='%.2f%%', startangle=90,
        #                                 pctdistance=0.85, explode=self.explode[:len(self.values)])

        # # add a circle to create a pie chart
        
        # # plt.axis('equal')    
        # # plt.legend(loc='upper left')

        # centre_circle = plt.Circle((0, 0), 0.70, fc='none')
        # self.ax.add_artist(centre_circle)
        # self.canvas_d = FigureCanvas(fig)
        # canvas.setStyleSheet("background-color: red;")
        # self.canvas.patch.set_facecolor('#244D54')
        self.fig.patch.set_facecolor('none')
        # add the canvas to the PyQt5 widget
        layout = QtWidgets.QVBoxLayout(self.widget_2)
        layout.addWidget(self.canvas_d)

        # self.create_donutchart()
        self.horizontalLayout_7.addWidget(self.widget_2)
        self.verticalLayout_12.addWidget(self.frame_10)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.horizontalLayout_6.addWidget(self.frame_dash_page)
        self.stackedWidget.addWidget(self.dashbord_page)

        # self.timer_dashboard = QTimer()
        # self.timer_dashboard.timeout.connect(self.show_data)
        # self.timer_dashboard.timeout.connect(self.update_dashboard_plot)
        # self.timer_dashboard.start(1000)

        # Soundpad Page
        self.filenames = []
        self.play_counts = {}
        self.player = QMediaPlayer()
        self.ui_main = ui_main

        self.Soundpad_page = QtWidgets.QWidget()
        self.Soundpad_page.setObjectName("Soundpad_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Soundpad_page)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SP_body = QtWidgets.QFrame(self.Soundpad_page)
        self.SP_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_body.setFrameShadow(QtWidgets.QFrame.Raised)

        # frame body layout
        self.SP_body.setObjectName("SP_body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.SP_body)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # Soundpad Title
        self.SP_title = QtWidgets.QFrame(self.SP_body)
        self.SP_title.setMinimumSize(QtCore.QSize(900, 120))
        self.SP_title.setMaximumSize(QtCore.QSize(900, 120))
        self.SP_title.setStyleSheet("QFrame{\n"
                                    "    background-color: rgba(0, 0, 0, 0);\n"
                                    "}")
        self.SP_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_title.setObjectName("SP_title")

        # Soundpad Title Layout
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.SP_title)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.SP_title)
        # self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.SP_title_label = QtWidgets.QLabel(self.SP_title)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.SP_title_label.setFont(font)
        self.SP_title_label.setStyleSheet("QLabel \n"
                                          "{\n"
                                          " color: #FFFFFF;\n"
                                          "}")
        self.SP_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SP_title_label.setObjectName("SP_title_label")

        self.horizontalLayout_6.addWidget(self.SP_title_label)
        self.DasB_pushButton = QtWidgets.QPushButton(self.SP_title)
        self.DasB_pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.DasB_pushButton.setMaximumSize(QtCore.QSize(50, 50))
        # self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DasB_pushButton.setObjectName("pushButton")
        icon_dash = QtGui.QIcon()
        icon_dash.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/DB_piechart4.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.DasB_pushButton.setStyleSheet("QFrame{\n"
        #                            "    padding-right: 20px\n"
        #                            "}")

        # DAshboad button clicked
        # self.pushButton.clicked.connect()

        self.DasB_pushButton.setIcon(icon_dash)
        self.DasB_pushButton.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout_6.addWidget(self.DasB_pushButton)
        # self.verticalLayout_7.addWidget(self.SP_title_label)
        self.verticalLayout_6.addWidget(self.SP_title)
        self.SP_item = QtWidgets.QFrame(self.SP_body)
        self.SP_item.setStyleSheet("QFrame{\n"
                                   "    background-color: rgba(0, 0, 0, 0);\n"
                                   "}")

        # Soundpad item
        self.SP_item.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_item.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_item.setObjectName("SP_item")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.SP_item)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        # Table Layout
        self.SP_table = QtWidgets.QFrame(self.SP_item)
        self.SP_table.setMinimumSize(QtCore.QSize(830, 470))
        self.SP_table.setMaximumSize(QtCore.QSize(830, 470))
        self.SP_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_table.setObjectName("SP_table")
        self.SP_table.setStyleSheet("QFrame{\n"
                                    "    background-color: rgba(0, 0, 0, 0);\n"
                                    "}")

        # Soundpad Table Layout
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SP_table)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SP_scrollArea = QtWidgets.QScrollArea(self.SP_table)
        self.SP_scrollArea.setStyleSheet(
            "QScrollBar:vertical {\n"
            "border: none;\n"
            "background: #244D54;\n"
            "width: 14px;\n"
            "margin: 15px 0 15px 0;\n"
            "border-radius: 0px;\n"
            " }\n"
            "\n"
            "/*  HANDLE BAR VERTICAL */\n"
            "QScrollBar::handle:vertical {    \n"
            "background-color: #56B7C7;\n"
            "min-height: 80px;\n"
            "border-radius: 7px;\n"
            "}\n"
            "\n"
            "/* BTN TOP - SCROLLBAR */\n"
            "QScrollBar::sub-line:vertical {\n"
            "border: none;\n"
            "background-color: #244D54;\n"
            "height: 15px;\n"
            "border-top-left-radius: 7px;\n"
            "border-top-right-radius: 7px;\n"
            "subcontrol-position: top;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "/* BTN BOTTOM - SCROLLBAR */\n"
            "QScrollBar::add-line:vertical {\n"
            "border: none;\n"
            "background-color: #244D54;\n"
            "height: 15px;\n"
            "border-bottom-left-radius: 7px;\n"
            "border-bottom-right-radius: 7px;\n"
            "subcontrol-position: bottom;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "/* RESET ARROW */\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "background: none;\n"
            "}\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "background: none;\n"
            "}"
        )
        self.SP_scrollArea.setWidgetResizable(True)
        self.SP_scrollArea.setObjectName("SP_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 830, 470))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.SP_scrollArea.horizontalScrollBar().hide()
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")

        # Table Widget
        self.SP_tableWidget = QtWidgets.QTableWidget(
            self.scrollAreaWidgetContents)
        self.SP_tableWidget.setStyleSheet("")
        self.SP_tableWidget.setObjectName("SP_tableWidget")
        # self.SP_tableWidget.setColumnCount(5)
        # self.SP_tableWidget.setRowCount(9)

        # self.SP_tableWidget.setRowCount(3)
        self.SP_tableWidget.setColumnCount(5)
        self.SP_tableWidget.setHorizontalHeaderLabels(
            ['Name', 'Duration', '', 'Status', ''])
        self.SP_tableWidget.verticalHeader().hide()
        # effect = QGraphicsDropShadowEffect()
        # self.SP_tableWidget.setGraphicsEffect(effect)
        # self.SP_tableWidget.setStyleSheet("QHeaderView {\n"
        #                                "color: #56B7C7;\n"
        #                             #    "text-style; bold\n"
        #                             #    "text-shadow: 2px 2px;\n"
        #                             #    "border: 0px solid  # 567dbc;\n"
        #                             #    "border-left: 0px;\n"
        #                             #    "border-right: 0px;\n"
        #                             #    "background:  # f9f9f9;\n"
        #                                "}"
        #                                )
        # self.Testmic_button.setStyleSheet("QPushButton{\n"
        #                                   "    background-color: #244D54;\n"
        #                                   "    border-style : outset;\n"
        #                                   "    border-width : 0.5px;\n"
        #                                   "    border-radius: 25px;\n"
        #                                   "    border-color : black;\n"
        #                                   "\n"
        #                                   "    color: #686868;\n"
        #                                   "    text-align : center;\n"
        #                                   "}\n"
        #                                   "QPushButton:hover{\n"
        #                                   "    background-color: #35707A;    \n"
        #                                   "    border-width : 0.5px;\n"
        #                                   "    border-color :  rgb(1, 209, 158) ;\n"
        #                                   "    color: rgb(204, 204, 204);\n"
        #                                   "}\n"
        #                                   )
        self.SP_tableWidget.setStyleSheet("QTableWidget::item {"
                                          "color: #d7d7d7;"
                                          "background-color: rgba(50, 75, 79, 140)"
                                          #   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(138, 138, 138, 50), stop:0.886364 rgba(102, 218, 237, 255));"
                                          "}"
                                          "QTableWidget{"
                                          "gridline-color:  transparent;"
                                          "padding-left: 56px;\n"
                                          "}"
                                          )
        self.SP_tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section { font-size: 10pt;"
                                                             "font-weight: bold;"
                                                             "color: #56B7C7;"
                                                             "background-color: transparent;"
                                                             "}"
                                                             "QHeaderView {"
                                                             "border-bottom: 1px solid #00FFF0;"
                                                             "}")

        self.SP_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.SP_tableWidget.horizontalHeader().setDisabled(True)
        self.SP_tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.SP_tableWidget.autofit = False
        self.SP_tableWidget.setColumnWidth(0, 401)
        self.SP_tableWidget.setColumnWidth(1, 131)
        self.SP_tableWidget.setColumnWidth(2, 81)
        self.SP_tableWidget.setColumnWidth(3, 80)
        self.SP_tableWidget.setColumnWidth(4, 80)

        try:
            with open("soundpad.pickle", "rb") as file:
                sp_data = pickle.load(file)
                for fname, count in sp_data.items():
                    self.filenames.append(fname)
                    self.play_counts[fname] = count

                    row = self.SP_tableWidget.rowCount()
                    self.SP_tableWidget.insertRow(row)

                    self.SP_tableWidget.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))

                    duration = self.getDuration(fname)
                    self.SP_tableWidget.setItem(row, 1, QTableWidgetItem(duration))   

                    play_button = self.play_button(fname, row)
                    self.SP_tableWidget.setCellWidget(row, 2, play_button)

                    self.SP_tableWidget.setCellWidget(row, 3, self.listen_button("", fname))

                    remove_button = self.remove_button(row, fname)

                    self.SP_tableWidget.setCellWidget(row, 4, remove_button)
                    # remove_button.clicked.connect(lambda _, r=row, f=fname: self.remove_file(r, f))

                print("audio load successfully")

                print("audio load successfully")

        except Exception as e:
            print("Error loading audio files:", e)

        # for index in range(self.SP_tableWidget.rowCount()):

        #     # play button
        #     self.btn_play = QPushButton(self.SP_tableWidget)
        #     self.btn_play.setText('Play')
        #     self.SP_tableWidget.setCellWidget(index, 4, self.btn_play)
        #     self.btn_play.clicked.connect(
        #         lambda: self.SP_play_item(self.SP_tableWidget.currentRow()))

        #     # listen button
        #     self.btn_listen = QPushButton(self.SP_tableWidget)
        #     self.btn_listen.setText('Listen')
        #     self.SP_tableWidget.setCellWidget(index, 5, self.btn_listen)
        #     self.btn_listen.clicked.connect(
        #         lambda: self.SP_listen_item(self.SP_tableWidget.currentRow()))

        #     # delete button
        #     self.btn_delete = QPushButton(self.SP_tableWidget)
        #     self.btn_delete.setText('delete')
        #     self.SP_tableWidget.setCellWidget(index, 6, self.btn_delete)
        #     self.btn_delete.clicked.connect(
        #         lambda: self.remove_file(self.SP_tableWidget.currentRow()))

        self.verticalLayout_15.addWidget(self.SP_tableWidget)
        self.SP_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.SP_scrollArea)
        self.verticalLayout_8.addWidget(self.SP_table)

        # Soundpad botton Area
        self.SP_botton_area = QtWidgets.QFrame(self.SP_item)
        self.SP_botton_area.setMinimumSize(QtCore.QSize(900, 130))
        self.SP_botton_area.setMaximumSize(QtCore.QSize(900, 130))
        self.SP_botton_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_botton_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_botton_area.setObjectName("SP_botton_area")
        self.SP_add_button = QtWidgets.QPushButton(self.SP_botton_area)

        # Soundpad add item button
        self.SP_add_button.clicked.connect(self.SP_add_item)

        self.SP_add_button.setGeometry(QtCore.QRect(760, 5, 100, 100))
        self.SP_add_button.setStyleSheet("QPushButton {\n"
                                         "    background: #56B7C7;\n"
                                         "    border-radius: 50px;\n"
                                         "    }\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background: #66DAED;\n"
                                         "    padding: 5px;\n"
                                         "    }\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background: #56B7C7;\n"
                                         "    padding: 5px;\n"
                                         "    }")
        self.SP_add_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/add8.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SP_add_button.setIcon(icon4)
        self.SP_add_button.setIconSize(QtCore.QSize(40, 40))
        self.SP_add_button.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.SP_botton_area)
        self.verticalLayout_6.addWidget(self.SP_item)
        self.horizontalLayout_4.addWidget(self.SP_body)
        self.stackedWidget.addWidget(self.Soundpad_page)

        # Voice Changer Page
        self.Voicechanger_page = QtWidgets.QWidget()
        self.VC_frame = QtWidgets.QFrame(self.Voicechanger_page)

        # Voice Changer Frame
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Voicechanger_page)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.VC_frame = QtWidgets.QFrame(self.Voicechanger_page)
        self.VC_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_frame.setObjectName("VC_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.VC_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Voice Changer Body
        self.VC_item_frame = QtWidgets.QFrame(self.VC_frame)
        self.VC_item_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_item_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_item_frame.setObjectName("VC_item_frame")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.VC_item_frame)
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName("verticalLayout_53")

        # Voice Changer Title
        self.VC_item_body = QtWidgets.QFrame(self.VC_item_frame)
        self.VC_item_body.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.VC_item_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_item_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_item_body.setObjectName("VC_item_body")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.VC_item_body)
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.VC_title_2 = QtWidgets.QFrame(self.VC_item_body)
        self.VC_title_2.setMinimumSize(QtCore.QSize(900, 120))
        self.VC_title_2.setMaximumSize(QtCore.QSize(900, 120))
        self.VC_title_2.setStyleSheet("QFrame{\n"
                                      "    background-color: rgba(0, 0, 0, 0);\n"
                                      "}")
        self.VC_title_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_title_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_title_2.setObjectName("VC_title_2")

        # Voice Changer Title Label
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.VC_title_2)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.VC_title_label_2 = QtWidgets.QLabel(self.VC_title_2)
        self.VC_title_label_2.setMinimumSize(QtCore.QSize(900, 0))
        self.VC_title_label_2.setMaximumSize(QtCore.QSize(900, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.VC_title_label_2.setFont(font)
        self.VC_title_label_2.setStyleSheet("QLabel \n"
                                            "{\n"
                                            " color: #FFFFFF;\n"
                                            "}")
        self.VC_title_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.VC_title_label_2.setObjectName("VC_title_label_2")
        self.verticalLayout_55.addWidget(self.VC_title_label_2)
        self.verticalLayout_54.addWidget(self.VC_title_2)

        # Voice Changer item
        self.VC_item = QtWidgets.QFrame(self.VC_item_body)
        self.VC_item.setMinimumSize(QtCore.QSize(900, 470))
        self.VC_item.setMaximumSize(QtCore.QSize(900, 470))
        self.VC_item.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_item.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_item.setObjectName("VC_item")

        # Voice Changer button
        self.gridLayout = QtWidgets.QGridLayout(self.VC_item)
        self.gridLayout.setContentsMargins(16, 8, 16, 8)
        self.gridLayout.setHorizontalSpacing(32)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")

        # Voice Changer button 2
        self.Voicechange_2 = QtWidgets.QPushButton(self.VC_item) #//TODO:

        self.Voicechange_2.setMinimumSize(QtCore.QSize(200, 170))
        self.Voicechange_2.setMaximumSize(QtCore.QSize(200, 170))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Voicechange_2.setFont(font)
        self.Voicechange_2.setStyleSheet("QPushButton {\n"
                                        "    background-color: #56B7C7;\n"
                                        "    border-radius: 20px;\n"
                                        "    \n"
                                        "    color: #000000;\n"
                                        "    text-align: center;\n"
                                        "    text:24px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color : #FFFFFF;\n"
                                        "    background-color : #4593A0 ;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-color:#00D19D ;\n"
                                        "    border-width : 2px;\n"
                                        "    border-style: outset;\n"
                                        "}")
        self.Voicechange_2.setObjectName("Voicechange_2")
        self.gridLayout.addWidget(self.Voicechange_2, 0, 1, 1, 1)

        # Voice Changer button 2 function
        self.Voicechange_2.clicked.connect(self.VC_item_2_clicked)

        # Voice Changer button 4
        self.Voicechange_4 = QtWidgets.QPushButton(self.VC_item)

        self.Voicechange_4.setMinimumSize(QtCore.QSize(200, 170))
        self.Voicechange_4.setMaximumSize(QtCore.QSize(200, 170))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Voicechange_4.setFont(font)
        self.Voicechange_4.setStyleSheet("QPushButton {\n"
                                        "    background-color: #56B7C7;\n"
                                        "    border-radius: 20px;\n"
                                        "    \n"
                                        "    color: #000000;\n"
                                        "    text-align: center;\n"
                                        "    text:24px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color : #FFFFFF;\n"
                                        "    background-color : #4593A0 ;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-color:#00D19D ;\n"
                                        "    border-width : 2px;\n"
                                        "    border-style: outset;\n"
                                        "}")
        self.Voicechange_4.setObjectName("Voicechange_4")
        self.gridLayout.addWidget(self.Voicechange_4, 1, 0, 1, 1)

        # Voice Changer button 4 function
        self.Voicechange_4.clicked.connect(self.VC_item_4_clicked)

        # Voice Changer button 1
        self.Voicechange_1 = QtWidgets.QPushButton(self.VC_item)
        self.Voicechange_1.setMinimumSize(QtCore.QSize(200, 170))
        self.Voicechange_1.setMaximumSize(QtCore.QSize(200, 170))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Voicechange_1.setFont(font)
        self.Voicechange_1.setStyleSheet("QPushButton {\n"
                                        "    background-color: #56B7C7;\n"
                                        "    border-radius: 20px;\n"
                                        "    \n"
                                        "    color: #000000;\n"
                                        "    text-align: center;\n"
                                        "    text:24px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color : #FFFFFF;\n"
                                        "    background-color : #4593A0 ;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-color:#00D19D ;\n"
                                        "    border-width : 2px;\n"
                                        "    border-style: outset;\n"
                                        "}")
        self.Voicechange_1.setObjectName("Voicechange_1")
        self.gridLayout.addWidget(self.Voicechange_1, 0, 0, 1, 1)

        # Voice Changer button function
        self.Voicechange_1.clicked.connect(self.VC_item_1_clicked)

        # Voice Changer button 3
        self.Voicechange_3 = QtWidgets.QPushButton(self.VC_item)

        self.Voicechange_3.setMinimumSize(QtCore.QSize(200, 170))
        self.Voicechange_3.setMaximumSize(QtCore.QSize(200, 170))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Voicechange_3.setFont(font)
        self.Voicechange_3.setStyleSheet("QPushButton {\n"
                                        "    background-color: #56B7C7;\n"
                                        "    border-radius: 20px;\n"
                                        "    \n"
                                        "    color: #000000;\n"
                                        "    text-align: center;\n"
                                        "    text:24px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color : #FFFFFF;\n"
                                        "    background-color : #4593A0 ;\n"
                                        "    border-width: 0.5px;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-color:#00D19D ;\n"
                                        "    border-width : 2px;\n"
                                        "    border-style: outset;\n"
                                        "}")
        self.Voicechange_3.setObjectName("Voicechange_3")
        self.gridLayout.addWidget(self.Voicechange_3, 0, 2, 1, 1)

        # Voice Changer button 3 function
        self.Voicechange_3.clicked.connect(self.VC_item_3_clicked)

        self.verticalLayout_54.addWidget(self.VC_item)

        # Test Mic Button
        self.VC_Testmic = QtWidgets.QFrame(self.VC_item_body)

        self.VC_Testmic.setMinimumSize(QtCore.QSize(900, 130))
        self.VC_Testmic.setMaximumSize(QtCore.QSize(900, 130))
        self.VC_Testmic.setStyleSheet("QFrame{\n"
                                      "    background-color: rgba(0, 0, 0, 0);\n"
                                      "\n"
                                      "    padding-left: 60px;\n"
                                      "    padding-right: 60px;\n"
                                      "    padding-top: 0px;\n"
                                      "    padding-bottom: 20px;\n"
                                      "}")

        self.VC_Testmic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Testmic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Testmic.setObjectName("VC_Testmic")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.VC_Testmic)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.VC_Testmi_button = QtWidgets.QPushButton(self.VC_Testmic)

        # Test Mic Button Function
        self.VC_Testmi_button.clicked.connect(self.VC_Testmi_button_clicked)

        self.VC_Testmi_button.setMinimumSize(QtCore.QSize(780, 80))
        self.VC_Testmi_button.setMaximumSize(QtCore.QSize(780, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.VC_Testmi_button.setFont(font)
        self.VC_Testmi_button.setStyleSheet("QPushButton {\n"
                                            "    background-color: #244D54;\n"
                                            "    border-style: outset;\n"
                                            "    border-width: 0.5px;\n"
                                            "    border-radius: 25px;\n"
                                            "    border-color: black;\n"
                                            "    \n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    text-align: center;\n"
                                            "\n"
                                            "    padding: 20px\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "    border-width : 0.5px;\n"
                                            "    border-color :  rgb(1, 209, 158) ;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color: #244D54;\n"
                                            "    border-style : inset;\n"
                                            "    border-width : 2px;\n"
                                            "    border-color : #00D19D;\n"
                                            "    color: #FFFFFF;\n"
                                            "}")
        self.VC_Testmi_button.setObjectName("VC_Testmi_button")
        self.verticalLayout_12.addWidget(self.VC_Testmi_button)
        self.verticalLayout_54.addWidget(self.VC_Testmic)
        self.verticalLayout_53.addWidget(self.VC_item_body)
        self.horizontalLayout_6.addWidget(self.VC_item_frame)
        self.horizontalLayout_5.addWidget(self.VC_frame)
        self.stackedWidget.addWidget(self.Voicechanger_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(20, 400, 171, 61))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(ui_main)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ui_main)

    def updateInput_now(self, value):
        print(value)
        self.device = self.devicesInput_list.index(value)
        # print('Device:',self.devicesInput_list.index(value))

    def updateOutput_now(self, value):
        print(value)
        self.device1 = self.devicesOutput_list.index(value)
        # print('Speaker:',self.devicesOutput_list.index(value))

    def volume_mute(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        if (Ui_mainInterface.audio_mute == 0):
            print("Volume Mute")
            Ui_mainInterface.audio_mute = 1
            volume.SetMute(1, None)
            icon_volume_mute = QtGui.QIcon()
            icon_volume_mute.addPixmap(QtGui.QPixmap(
                "Frontend/Pyqt6/icons/mutespeaker-sai8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_mute)

        else:
            print("Volume UnMute")
            Ui_mainInterface.audio_mute = 0
            volume.SetMute(0, None)
            icon_volume_unmute = QtGui.QIcon()
            icon_volume_unmute.addPixmap(QtGui.QPixmap(
                "Frontend/Pyqt6/icons/unmutespeaker-sai8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_unmute)

    def mic_mute(self):
        if (Ui_mainInterface.microphone_mute == 0):
            print("Mic Mute")
            Ui_mainInterface.microphone_mute = 1
            icon_mic_mute = QtGui.QIcon()
            icon_mic_mute.addPixmap(QtGui.QPixmap(
                "Frontend/Pyqt6/icons/mutemic-sai8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.micmute.setIcon(icon_mic_mute)

        else:
            print("Mic UnMute")
            Ui_mainInterface.microphone_mute = 0
            icon_mic_unmute = QtGui.QIcon()
            icon_mic_unmute.addPixmap(QtGui.QPixmap(
                "Frontend/Pyqt6/icons/mic-sai8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.micmute.setIcon(icon_mic_unmute)

    def updateboostmicl(self, value):
        if value == 0:
            Ui_mainInterface.microphone_mute = 1
            icon_mic_mute = QtGui.QIcon()
            icon_mic_mute.addPixmap(QtGui.QPixmap(
                "Frontend/Pyqt6/icons/mutemic-sai8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.micmute.setIcon(icon_mic_mute)
        else:
            Ui_mainInterface.microphone_mute = 0
            icon_mic_unmute = QtGui.QIcon()
            icon_mic_unmute.addPixmap(QtGui.QPixmap(
                "Frontend/Pyqt6/icons/mic-sai8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.micmute.setIcon(icon_mic_unmute)

    def get_volume(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        return cast(interface, POINTER(IAudioEndpointVolume))

    def open_device(self):
        subprocess.run(["control", "mmsys.cpl"])

    def updatevolume(self, value):
        self.volume.SetMasterVolumeLevelScalar(
            self.horizontalSlider.value() / 100, None)

        if value == 0:
            Ui_mainInterface.audio_mute = 1
            icon_volume_mute = QtGui.QIcon()
            icon_volume_mute.addPixmap(QtGui.QPixmap(
                "Frontend/Pyqt6/icons/mutespeaker-sai8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_mute)
            self.volume.SetMute(1, None)
        else:
            Ui_mainInterface.audio_mute = 0
            icon_volume_unmute = QtGui.QIcon()
            icon_volume_unmute.addPixmap(QtGui.QPixmap(
                "Frontend/Pyqt6/icons/unmutespeaker-sai8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_unmute)
            self.volume.SetMute(0, None)

    def retranslateUi(self, ui_main):
        _translate = QtCore.QCoreApplication.translate
        ui_main.setWindowTitle(_translate("ui_main", "EchoEcho"))
        # Window_icon = QtGui.QIcon('Frontend/Pyqt6/icons/SP_play_icon.png')
        ui_main.setWindowIcon(QtGui.QIcon('Frontend/Pyqt6/icons/logo_App.png'))
        self.Microphone_button.setText(_translate("ui_main", "Microphone"))
        # Test
        # self.Alert_button.setText(_translate("ui_main", "Test"))

        self.Soundpad_button.setText(_translate("ui_main", "Soundpad"))
        self.Voicechanger_button.setText(_translate("ui_main", "Voicechanger"))
        self.Mic_title_label.setText(_translate("ui_main", "Microphone"))
        self.setting_Button.setText(_translate("ui_main", "Setting"))
        self.Noise_button.setText(_translate("ui_main", "\n"
                                             "detecting the sound coming into the headset, and generating signals \n"
                                             "that are  out-of-phase with the  offending signals, canceling them out."))
        self.Noise_label.setText(_translate("ui_main", "Noise Suppression"))
        # self.label.setText(_translate("ui_main", "Graph_text"))
        self.Testmic_button.setText(_translate("ui_main", "Test Microphone"))
        # self.audio_label.setText(_translate("ui_main", "Audio"))
        self.SP_title_label.setText(_translate("ui_main", "Soundpad"))

        self.VC_title_label_2.setText(_translate("ui_main", "Voicechanger"))
        self.Voicechange_2.setText(_translate("ui_main", "Sudlor"))
        self.Voicechange_4.setText(_translate("ui_main", "Robot"))
        self.Voicechange_1.setText(_translate("ui_main", "Chipmunk"))
        self.Voicechange_3.setText(_translate("ui_main", "GigaChad"))
        self.VC_Testmi_button.setText(_translate("ui_main", "Test Microphone"))

        self.dash_label.setText(_translate("ui_main", "Dashboard"))
        # self.VoiceChanger_label.setText(_translate("ui_main", "VoiceChanger"))
        self.settingmain.setText(_translate("ui_main", "Settings"))
        self.detaildefault.setHtml(_translate("ui_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#cccccc;\">CURRENT VERSION:</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600; color:#cccccc;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#cccccc;\">EchoEcho App: 1.0.1</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.detailequipment.setHtml(_translate("ui_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#cccccc;\">Open control panel sound card setting.</span></p></body></html>"))
        self.Equipmentsetting.setText(
            _translate("ui_main", "Equipment setting"))
        self.Tutorial.setText(_translate("ui_main", "Tutorial"))
        self.settingButton.setText(_translate("ui_main", "Setting"))

    # Alert button clicked function
        # self.label.setText(_translate(
        #     "ui_main", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">No audio output device found</span></p></body></html>")) #//TODO:
        # self.Alert_button_detail.setText(_translate(
        #     "ui_main", "Check your audio output device and try again")) 

        self.label.setText(_translate(
            "ui_main", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">No virtual cable found</span></p></body></html>"))  # //TODO:
        self.Alert_button_detail.setText(_translate(
            "ui_main", "Check your virtual cable or install from vb-audio.com"))

    # Alert button clicked function
    def Alert_button_detail_clicked(self):
        print("Alert button clicked")

        self.settingmain.setText(_translate("ui_main", "Settings"))
        self.detaildefault.setHtml(_translate("ui_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#cccccc;\">CURRENT VERSION:</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600; color:#cccccc;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#cccccc;\">EchoEcho App: 1.0.1</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.detailequipment.setHtml(_translate("ui_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#cccccc;\">Open control panel sound card setting.</span></p></body></html>"))
        self.Equipmentsetting.setText(
            _translate("ui_main", "Equipment setting"))
        self.Tutorial.setText(_translate("ui_main", "Tutorial"))
        self.settingButton.setText(_translate("ui_main", "Setting"))

    # Side menu button clicked
    ##############################
    def Mic_Side_menu_clicked(self):
        # Mic clciked
        ##############################
        if (Ui_mainInterface.Mic_Side_menu == 0):
            # print("MIC clicked")
            Ui_mainInterface.Mic_Side_menu = 1
            Ui_mainInterface.SP_Side_menu = 0
            Ui_mainInterface.VC_Side_menu = 0
            self.Microphone_button.setStyleSheet("QPushButton {\n"
                                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                                 "}")
            self.Soundpad_button.setStyleSheet("QPushButton{\n"
                                               "    background-color: rgba(0, 0, 0, 0)\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                               "}")
            self.Voicechanger_button.setStyleSheet("QPushButton{\n"
                                                   "    background-color: rgba(0, 0, 0, 0)\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                                   "}")

    def SP_Side_menu_clicked(self):
        # SP clicked
        ##############################
        if (Ui_mainInterface.SP_Side_menu == 0):
            # print("SP clicked")
            Ui_mainInterface.SP_Side_menu = 1
            Ui_mainInterface.Mic_Side_menu = 0
            Ui_mainInterface.VC_Side_menu = 0
            self.Soundpad_button.setStyleSheet("QPushButton {\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                               "}")
            self.Microphone_button.setStyleSheet("QPushButton{\n"
                                                 "    background-color: rgba(0, 0, 0, 0)\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                                 "}")
            self.Voicechanger_button.setStyleSheet("QPushButton{\n"
                                                   "    background-color: rgba(0, 0, 0, 0)\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                                   "}")

    def VC_Side_menu_clicked(self):
        # VC clicked
        ##############################
        if (Ui_mainInterface.VC_Side_menu == 0 or Ui_mainInterface.Mic_Side_menu == 1 or Ui_mainInterface.SP_Side_menu == 1):
            # print("VC clicked")
            Ui_mainInterface.VC_Side_menu = 1
            Ui_mainInterface.Mic_Side_menu = 0
            Ui_mainInterface.SP_Side_menu = 0
            self.Voicechanger_button.setStyleSheet("QPushButton {\n"
                                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                                   "}")
            self.Microphone_button.setStyleSheet("QPushButton{\n"
                                                 "    background-color: rgba(0, 0, 0, 0)\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                                 "}")
            self.Soundpad_button.setStyleSheet("QPushButton{\n"
                                               "    background-color: rgba(0, 0, 0, 0)\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                               "}")

    # ปุ่มเปิดปิด Noise Suppression and test microphone
    #############################################

    def Noise_button_clicked(self):
        # print("Noise button clicked")
        if (Ui_mainInterface.noise_reduce == 0):
            Ui_mainInterface.noise_reduce = 1
            self.current_plot = 'reduce'
            print("current plot = ", self.current_plot)

            # ทำให้ปุ่มเปิด
            self.Noise_button.setStyleSheet("QPushButton{\n"
                                            "    border-radius: 40px;\n"
                                            "    background-color: #244D54;\n"
                                            "    border-style : inset;\n"
                                            "    border-width : 2px;\n"
                                            "\n"
                                            "    border-color : #00D19D;\n"
                                            "    color: #FFFFFF;\n"
                                            "}"
                                            )
            self.stream = self.pa.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,
                                       frames_per_buffer=self.CHUNK_SIZE, stream_callback=self.reduce_audio_callback)
            for line in self.lines:
                line.remove()
            self.lines = self.ax.plot(self.plot_data)
            # self.CALLBACK = self.reduce_audio_callback
            self.PLOT = self.reduce_update_plot
        else:
            Ui_mainInterface.noise_reduce = 0
            self.current_plot = 'normal'

            print("current plot = ", self.current_plot)
            # ทำปุ่มปิด
            self.Noise_button.setStyleSheet("QPushButton{\n"
                                            "    background-color: #244D54;\n"
                                            "    border-style : outset;\n"
                                            "    border-width : 0.5px;\n"
                                            "    border-radius: 40px;\n"
                                            "    border-color : black;\n"
                                            "\n"
                                            "    color: #686868;\n"
                                            "    text-align : center;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: #35707A;    \n"
                                            "    border-width : 0.5px;\n"
                                            "    border-color :  rgb(1, 209, 158) ;\n"
                                            "    color: #B0B0B0;\n"
                                            "}"
                                            )
            self.stream = self.pa.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,
                                       frames_per_buffer=self.CHUNK_SIZE, stream_callback=self.normal_audio_callback)
            for line in self.lines:
                line.remove()
            self.lines = self.ax.plot(self.plot_data)
            # self.CALLBACK = self.normal_audio_callback
            self.PLOT = self.normal_update_plot
        self.timer.stop()
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.PLOT)
        self.timer.start(30)
    #############################################

    def TestMic_button_clicked(self):
        # print("Test mic button clicked")
        if (Ui_mainInterface.test_microphone == 0):
            Ui_mainInterface.test_microphone = 1
            # ทำให้ปุ่มเปิด
            self.Testmic_button.setStyleSheet("QPushButton{\n"
                                              "    border-radius: 25px;\n"
                                              "    background-color: #244D54;\n"
                                              "    border-style : inset;\n"
                                              "    border-width : 2px;\n"
                                              "    border-color : #00D19D;\n"
                                              "    color: #FFFFFF;\n"
                                              "}"
                                              )
        else:
            Ui_mainInterface.test_microphone = 0
            # ทำปุ่มปิด
            self.Testmic_button.setStyleSheet("QPushButton{\n"
                                              "    background-color: #244D54;\n"
                                              "    border-style : outset;\n"
                                              "    border-width : 0.5px;\n"
                                              "    border-radius: 25px;\n"
                                              "    border-color : black;\n"
                                              "\n"
                                              "    color: #686868;\n"
                                              "    text-align : center;\n"
                                              "}\n"

                                              "QPushButton:hover{\n"
                                              "    background-color: #35707A;    \n"
                                              "    border-width : 0.5px;\n"
                                              "    border-color :  rgb(1, 209, 158) ;\n"
                                              "    color: rgb(204, 204, 204);\n"
                                              "}"
                                              )

    # Soundpad Page Function
    # add item

    def SP_add_item(self, file_path):
        options = QFileDialog.Options()
        folder = r""

        fname, _ = QFileDialog.getOpenFileName(self.ui_main, "QFileDialog.getOpenFileName()", folder, "WAV Files (*.wav);; MP3 Files (*.mp3)", options=options)
        # fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", folder, "WAV or MP3 (*.wav *.mp3)", options=options) 

        if fname:
            if self.check_duplicate_file(fname):
                msg_box = QMessageBox()
                msg_box.setText("File name already exists.Please select another file or change file name.")
                msg_box.exec_()
                return
            
            print("add file :", fname)

            row = self.SP_tableWidget.rowCount()
            self.SP_tableWidget.insertRow(row)

            self.SP_tableWidget.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))

            # self.table.setItem(row, 1, QTableWidgetItem(""))
            # self.get_duration(QMediaPlayer.LoadedMedia, fname, row)


            duration = self.getDuration(fname)
            self.SP_tableWidget.setItem(row, 1, QTableWidgetItem(duration)) 

            
            play_button = self.play_button(fname, row)
            self.SP_tableWidget.setCellWidget(row, 2, play_button)
            # play_button.clicked.connect(lambda _, button=play_button, fname=fname, index=row: self.play_media(button, fname, index))

            self.SP_tableWidget.setCellWidget(row, 3, self.listen_button("", fname))

            remove_button = self.remove_button(row, fname)

            self.SP_tableWidget.setCellWidget(row, 4, remove_button)
            # remove_button.clicked.connect(lambda _, r=row, f=fname: self.remove_file(r, f))
            
            self.filenames.append(fname)

            if fname not in self.play_counts:
                self.play_counts[fname] = 0

            self.save_file()

        else:
            print("No file selected.")

    def check_duplicate_file(self, file_path):
        file_name = os.path.basename(file_path)
        if file_name in set([os.path.basename(fname) for fname in self.filenames]):
            return True
        return False

    def save_file(self):
        sp_data = {}
        for fname in self.filenames:
            sp_data[fname] = self.play_counts[fname]
            # sp_data[fname.split("/")[-1].split(".")[0]] = self.play_counts[fname]

        # save file in pickle
        with open("soundpad.pickle", "wb") as file:
            pickle.dump(sp_data, file)
        
        # self.play_counts[fname] = count
        
        print("save success")
        print(sp_data)

        sort_counts = sorted(self.play_counts.items(), key=lambda x: x[1], reverse=True)
        with open("sort_counts.txt", "w", encoding="utf-8") as file:
            for item in sort_counts:
                file.write(os.path.basename(item[0]) + "     Play counts : " + str(item[1]) + "\n")
    
        print("sort success")

    # play item
    
    # ========================================================================================================================================
    #//TODO:
    
    def play_button(self, fname, index):
        icon_play = QtGui.QIcon()
        icon_play.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/SP_play_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # play_button = QPushButton(text=str(label))
        # play_button.setIcon(icon_play)
        button = QPushButton(icon_play, "")
        button.setIconSize(QtCore.QSize(30, 30))
        # button.clicked.connect(lambda: self.play_media(button, fname, index))
        button.clicked.connect(lambda _, button=button: self.play_media(button, fname, index))
        
        # print("=====================================================")
        # print("show fname:", fname, "index: ", index)
        # print("=====================================================")
        return button

    def play_media(self, btn, fname, index):
        icon_pause = QtGui.QIcon()
        icon_pause.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/SP_pause_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_play = QtGui.QIcon()
        icon_play.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/SP_play_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # media_content = QMediaContent(QUrl.fromLocalFile(fname))
        media_content = fname
        # print("show fname:", fname)
        # if self.player.state() == QMediaPlayer.PlayingState and self.player.media().canonicalUrl() == media_content.canonicalUrl():
        #     self.player.stop()
        #     # play_button 
        #     btn.setIcon(icon_play)
        #     # btn.setText("play")
        global micplay
        global stop_threads
        global micplay_file
        if micplay == True and micplay_file == media_content:
            micplay = False
            stop_threads = True
            # play_button
            btn.setIcon(icon_play)
            # btn.setText("play")
            # print(micplay_file, " state : ", micplay)
        else:
            if micplay == True:
                curr_fname = micplay_file
                curr_btn = self.get_play(curr_fname)
                if curr_btn is not None:
                    curr_btn.setIcon(icon_play)
                    # curr_btn.setText("Play")
                # self.player.stop()
                micplay = False
                stop_threads = True

            for row in range(self.SP_tableWidget.rowCount()):
                item = self.SP_tableWidget.item(row, 0)
                if item is not None and item.text() != os.path.basename(fname):
                    play_btn = self.SP_tableWidget.cellWidget(row, 2)
                    if play_btn.setIcon(icon_pause) == btn.setIcon(icon_pause):
                        # self.player.stop()
                        micplay = False
                        stop_threads = True
                        play_btn.setIcon(icon_play)
                        # play_btn.setText("Play")

#==========================================================================
            # current_count = int(self.SP_tableWidget.item(self.SP_tableWidget.currentRow(), 4).text())
            # self.play_counts[fname] = current_count + 1  # บันทึกค่าเพิ่ม
            # current_count = int(self.play_counts.get(fname, 0)) + 1
            # self.play_counts[fname] = current_count
            # self.save_file() 
            # self.SP_tableWidget.item(self.SP_tableWidget.currentRow(), 4).setText(str(current_count + 1))

            # self.save_file()
            
            # self.player.setMedia(media_content)
            # self.player.play()

            micplay = True
            stop_threads = False
            micplay_file = media_content
            def runsound():
                wf = wave.open(media_content, "rb")
                sp_data = wf.readframes(1024)
                while len(sp_data) != 0:
                    ui_virtual_microphone_stream.write(sp_data)
                    sp_data = wf.readframes(1024)
                    if stop_threads:
                        break
            t1 = threading.Thread(target = runsound)
            t1.daemon = True
            t1.start()

            btn.setIcon(icon_pause)
            # btn.setText("Stop")
            current_count = int(self.play_counts.get(fname, 0)) + 1
            self.play_counts[fname] = current_count
            self.save_file() 

            # self.show_data()
            # self.update_dashboard_plot()

    def get_play(self, fname):
        for row in range(self.SP_tableWidget.rowCount()):
            if self.SP_tableWidget.item(row, 0).text() == os.path.basename(fname):
                return self.SP_tableWidget.cellWidget(row, 2)
            
    def listen_button(self, label, fname):
        icon_listen = QtGui.QIcon()
        icon_listen.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/SP_HP_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        listen_button = QPushButton(label)
        listen_button.setIcon(icon_listen)
        listen_button.setIconSize(QtCore.QSize(30, 30))
        listen_button.clicked.connect(lambda: self.listen_media(listen_button, fname))
        return listen_button

    def listen_media(self, btn, fname):
        icon_listen = QtGui.QIcon()
        icon_listen.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/SP_HP_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_pause = QtGui.QIcon()
        icon_pause.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/SP_pause_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        media_content = QMediaContent(QUrl.fromLocalFile(fname))
        if self.player.state() == QMediaPlayer.PlayingState and self.player.media().canonicalUrl() == media_content.canonicalUrl():
            self.player.stop()
            btn.setIcon(icon_listen)
            # btn.setText("")
        else:
            if self.player.state() == QMediaPlayer.PlayingState:
                curr_fname = self.player.currentMedia().canonicalUrl().toLocalFile()
                curr_btn = self.get_listen(curr_fname)
                if curr_btn is not None:
                    curr_btn.setIcon(icon_listen)
                    # curr_btn.setText("")
                self.player.stop()

            for row in range(self.SP_tableWidget.rowCount()):
                item = self.SP_tableWidget.item(row, 0)
                if item is not None and item.text() != os.path.basename(fname):
                    play_btn = self.SP_tableWidget.cellWidget(row, 3)
                    if play_btn.setIcon(icon_pause) == btn.setIcon(icon_pause):
                        self.player.stop()
                        play_btn.setIcon(icon_listen)
                        # play_btn.setText("")

            self.player.setMedia(media_content)
            self.player.play()
            btn.setIcon(icon_pause)
            # btn.setText("")

    def get_listen(self, fname):
        for row in range(self.SP_tableWidget.rowCount()):
            item = self.SP_tableWidget.item(row, 0)
            if item is not None and item.text() == os.path.basename(fname):
                return self.SP_tableWidget.cellWidget(row, 3)

    def getDuration(self, fname):
        if fname.endswith('.mp3'):
            audio = MP3(fname)
            duration = audio.info.length
        elif fname.endswith('.wav'):
            audio = WAVE(fname)
            duration = audio.info.length
        return time.strftime('%M:%S', time.gmtime(duration))

    # delete item button
    def remove_button(self, row, fname):
        icon_remove = QtGui.QIcon()
        icon_remove.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/SP_trash_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        remove_button = QPushButton()
        remove_button.setIcon(icon_remove)
        remove_button.setIconSize(QtCore.QSize(30, 30))
        remove_button.clicked.connect(lambda: self.confirm_remove_file(row, fname))
        return remove_button
    
    def confirm_remove_file(self, row, fname):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText(f"Are you sure you want to delete {fname}?")
        message_box.setWindowTitle("Confirm Deletion")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setDefaultButton(QMessageBox.No)
        response = message_box.exec()
        if response == QMessageBox.Yes:
            self.remove_file(row, fname)
        else:
            print("File removal cancelled.")

    def remove_file(self, row, fname):
        try:
            self.filenames.remove(fname)
            self.play_counts.pop(fname)
            for i in range(self.SP_tableWidget.rowCount()):
                if self.SP_tableWidget.item(i, 0).text() == os.path.basename(fname):
                    self.SP_tableWidget.removeRow(i)
                    break
            self.save_file()

            if self.player.state() == QMediaPlayer.PlayingState and self.player.currentMedia().canonicalUrl().toLocalFile() == fname:
                self.player.stop()

            print("File removed successfully.")

        except Exception as e:
            print("Error removing file:", e)

    def normal_audio_callback(self, in_data, frame_count, time_info, status):
        # Convert byte stream to numpy array
        # print("normal_callback")
        audio_data = np.frombuffer(in_data, dtype=np.float32)
        # Add new audio data to queue
        self.q_normal.put(audio_data)

        return (None, pyaudio.paContinue)

    def reduce_audio_callback(self, in_data, frame_count, time_info, status):
        # print("reduce_callback")
        # Convert byte stream to numpy array
        audio_data = np.frombuffer(in_data, dtype=np.float32)
        cutoff_low = 8000
        cutoff_high = 3000
        nyquist_rate = 44100 / 2.0
        pass_order = 5
        pass_stop = 40
        lowpass_coefficients = butter(
            pass_order, cutoff_low / nyquist_rate, btype='low', analog=False, output='sos')
        highpass_coefficients = butter(
            pass_stop, cutoff_high / nyquist_rate, btype='high', analog=False, output='sos')
        audio_frame = np.frombuffer(audio_data, dtype=np.float32)
        audio_frame = signal.decimate(audio_frame, 4, zero_phase=True)
        filtered_audio_lowpass = signal.sosfiltfilt(
            lowpass_coefficients, audio_frame)
        filtered_audio = signal.sosfiltfilt(
            highpass_coefficients, filtered_audio_lowpass)

        # Add new audio data to queue
        self.q_reduce.put(filtered_audio)
        return (None, pyaudio.paContinue)

    #########################################################
    # Voice Changer Page Function
    def VC_Testmi_button_clicked(self):
        print("VC Test mic button clicked")
        if (Ui_mainInterface.VC_test_microphone == 0):
            Ui_mainInterface.VC_test_microphone = 1
            # ทำให้ปุ่มเปิด
            self.VC_Testmi_button.setStyleSheet("QPushButton{\n"
                                                "    border-radius: 25px;\n"
                                                "    background-color: #244D54;\n"
                                                "    border-style : inset;\n"
                                                "    border-width : 2px;\n"
                                                "    border-color : #00D19D;\n"
                                                "    color: #FFFFFF;\n"
                                                "}"
                                                )
        else:
            Ui_mainInterface.VC_test_microphone = 0
            # ทำปุ่มปิด
            self.VC_Testmi_button.setStyleSheet("QPushButton{\n"
                                                "    background-color: #244D54;\n"
                                                "    border-style : outset;\n"
                                                "    border-width : 0.5px;\n"
                                                "    border-radius: 25px;\n"
                                                "    border-color : black;\n"
                                                "\n"
                                                "    color: #686868;\n"
                                                "    text-align : center;\n"
                                                "}\n"

                                                "QPushButton:hover{\n"
                                                "    background-color: #35707A;    \n"
                                                "    border-width : 0.5px;\n"
                                                "    border-color :  rgb(1, 209, 158) ;\n"
                                                "    color: rgb(204, 204, 204);\n"
                                                "}"
                                                )

    def normal_update_plot(self):
        # Get all the available audio data from the queue
        # print(self.q.qsize())
        if self.current_plot != 'normal':
            return
        while not self.q_normal.empty():
            # print("normal queue not empty")
            data = self.q_normal.get()
            # Downsample the data if needed
            # if self.DOWN_SAMPLE > 1:
            data = data[::6]

            # Update the plot data
            shift = len(data)
            self.plot_data = np.roll(self.plot_data, -shift, axis=0)
            self.plot_data[-shift:, :] = data[:, np.newaxis]

        # Update the plot lines with the new data
        for column, line in enumerate(self.lines):
            line.set_ydata(self.plot_data[:, column])
            line.set_color((1, 0, 0))
            self.canvas.draw()

    def reduce_update_plot(self):
        if self.current_plot != 'reduce':
            return
        # Get all the available audio data from the queue
        while not self.q_reduce.empty():
            # print("reduce queue not empty")
            data = self.q_reduce.get()
            # Downsample the data if needed
            # if self.DOWN_SAMPLE > 1:
            data = data[::self.DOWN_SAMPLE]

            # Update the plot data
            shift = len(data)
            self.plot_data = np.roll(self.plot_data, -shift, axis=0)
            self.plot_data[-shift:, :] = data[:, np.newaxis]

        # Update the plot lines with the new data
        for column, line in enumerate(self.lines):
            line.set_ydata(self.plot_data[:, column])
            line.set_color((0, 1, 0.29))
            self.canvas.draw()

    def VC_item_1_clicked(self):
        if (Ui_mainInterface.VC_item_1 == 0):
            print("VC item 1 clicked")
            Ui_mainInterface.VC_item_1 = 1
            Ui_mainInterface.VC_item_2 = 0
            Ui_mainInterface.VC_item_3 = 0
            Ui_mainInterface.VC_item_4 = 0
            self.Voicechange_1.setStyleSheet("QPushButton {\n"
                                         "color : #FFFFFF;\n"
                                         "background-color : #4593A0;\n"
                                         "border-width: 0.5px;\n"
                                         "border-radius: 20px;\n"
                                         "border-color:#00D19D;\n"
                                         "border-width : 2px;\n"
                                         "border-style: outset;\n"
                                         "}")
            self.Voicechange_2.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            self.Voicechange_3.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"

                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            self.Voicechange_4.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"

                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
        else :
            Ui_mainInterface.VC_item_1 = 0
            self.Voicechange_1.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            
    def VC_item_2_clicked(self):
        if (Ui_mainInterface.VC_item_2 == 0):
            print("VC item 2 clicked")
            Ui_mainInterface.VC_item_1 = 0
            Ui_mainInterface.VC_item_2 = 1
            Ui_mainInterface.VC_item_3 = 0
            Ui_mainInterface.VC_item_4 = 0
            self.Voicechange_2.setStyleSheet("QPushButton {\n"
                                         "color : #FFFFFF;\n"
                                         "background-color : #4593A0;\n"
                                         "border-width: 0.5px;\n"
                                         "border-radius: 20px;\n"
                                         "border-color:#00D19D;\n"
                                         "border-width : 2px;\n"
                                         "border-style: outset;\n"
                                         "}")
            self.Voicechange_1.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            self.Voicechange_3.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            self.Voicechange_4.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
        else :
            Ui_mainInterface.VC_item_2 = 0
            self.Voicechange_2.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
    
    def VC_item_3_clicked(self):
        if (Ui_mainInterface.VC_item_3 == 0):
            print("VC item 3 clicked")
            Ui_mainInterface.VC_item_1 = 0
            Ui_mainInterface.VC_item_2 = 0
            Ui_mainInterface.VC_item_3 = 1
            Ui_mainInterface.VC_item_4 = 0
            self.Voicechange_3.setStyleSheet("QPushButton {\n"
                                         "color : #FFFFFF;\n"
                                         "background-color : #4593A0;\n"
                                         "border-width: 0.5px;\n"
                                         "border-radius: 20px;\n"
                                         "border-color:#00D19D;\n"
                                         "border-width : 2px;\n"
                                         "border-style: outset;\n"
                                         "}")
            self.Voicechange_1.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            self.Voicechange_2.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            self.Voicechange_4.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
        else :
            Ui_mainInterface.VC_item_3 = 0
            self.Voicechange_3.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
    
    def VC_item_4_clicked(self):
        if (Ui_mainInterface.VC_item_4 == 0):
            print("VC item 4 clicked")
            Ui_mainInterface.VC_item_1 = 0
            Ui_mainInterface.VC_item_2 = 0
            Ui_mainInterface.VC_item_3 = 0
            Ui_mainInterface.VC_item_4 = 1
            self.Voicechange_4.setStyleSheet("QPushButton {\n"
                                         "color : #FFFFFF;\n"
                                         "background-color : #4593A0;\n"
                                         "border-width: 0.5px;\n"
                                         "border-radius: 20px;\n"
                                         "border-color:#00D19D;\n"
                                         "border-width : 2px;\n"
                                         "border-style: outset;\n"
                                         "}")
            self.Voicechange_1.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            self.Voicechange_2.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
            self.Voicechange_3.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
        else :
            Ui_mainInterface.VC_item_4 = 0
            self.Voicechange_4.setStyleSheet("QPushButton{\n"
                                         "background-color: #56B7C7;\n"
                                         "border-radius: 20px;\n"
                                         "color: #000000;\n"
                                         "text-align: center;\n"
                                         "}\n"
                                         
                                         "QPushButton:hover {\n"
                                         "background-color: #4593A0;\n"
                                         "border-radius: 20px;\n"
                                         "}")
    
    def show_data(self):
        # โหลดข้อมูลจากไฟล์ .txt และแสดงผลใน QTextEdit ของ frame_9
        try:
            with open('sort_counts.txt', 'r') as f:
                # sort_data = f.readlines()
                # sort_data = ''.join(sort_data[:3]).split('\n')
                # sort_data = '\n'.join(sort_data)
                # self.label_dash.setText(sort_data)

                sort_data = f.readlines()
                sort_data = [line.strip() for line in sort_data]
                sort_data = "\n".join([f"Top {i} : {line}" for i, line in enumerate(sort_data[:3], 1)])
                self.label_dash.setText(sort_data)

                if sort_data:
                    self.label_dash.setStyleSheet("background-color: rgba(0, 0, 0, 0.3);color: #fff; font-size: 21px;border: 3px solid #52ffff;border-radius: 10px; padding-left:15px;")
            
        except Exception as e:
            print("Error loading text file:",e)

        
    # def insert_ax(self):
    #     self.ax = self.canvas_d.figure.subplots()
    #     self.pie = None

    def update_dashboard_plot(self):
        # fig = Figure()
        # ax = fig.add_subplot(111)
        # self.canvas_d = FigureCanvas(self.fig)
        # self.fig.set_canvas(self.canvas_d)
        # self.ax_d.clear()
        # self.canvas_d.clear()
        # self.canvas_d.draw()  
        # self.SetSize((self.Size[0],self.canvas_d.Size[1]))
        # อ่านไฟล์ sort_counts.txt เพื่อใช้ในการสร้างกราฟ
        # self.ax_d.clear()

        with open('sort_counts.txt', 'r') as f:
            lines = f.readlines()

            data = {}
            texts = []
            for line in lines:
                line = line.strip()
                parts = line.split('     Play counts : ')
                text = parts[0]
                number = int(parts[1])
                data[text] = number
            self.colors = ['#B9DDF1', '#9FCAE6', '#73A4CA', '#497AA7', '#244D54', '#999999', '#C9C9C9']
            self.explode = (0, 0, 0, 0, 0, 0, 0)    
            self.labels = list(data.keys())[:7]
            self.values = list(data.values())[:7]
            # print("eeee", self.values)
        # create the donut plot 
            self.ax_d.clear()
            self.ax_d.pie(self.values, colors=self.colors,
                        autopct='%.2f%%', startangle=90,
                        pctdistance=0.85, explode=self.explode[:len(self.values)])  
            self.fig.subplots_adjust(bottom = -0.07, left = -0.4)   
            # if self.pie:
            #     self.pie.remove()    
            # self.pie = self.ax_d.pie(self.values, colors=self.colors, labels=self.labels,
            #                         autopct='%.2f%%', startangle=90,
            #                         pctdistance=0.85, explode=self.explode[:len(self.values)])
            # self.canvas_d.draw()

            centre_circle = plt.Circle((0, 0), 0.70, fc='none')
            self.ax_d.add_artist(centre_circle)
            if self.values:
                self.ax_d.legend(labels=self.labels, loc='upper right', bbox_to_anchor = (2, 0.85))
                title = self.ax_d.set_title("Chart Soundpad")
                title.set_fontsize(18)
                title.set_fontweight('semibold')
                title.set_color('white')
                title.set_position([1.05, 1])
            # self.canvas_d = FigureCanvas(self.fig)
            self.canvas_d.draw()
            # self.canvas_d.flush_events()

        # # add a circle to create a donut chart
        # centre_circle = plt.Circle((0, 0), 0.70, fc='none')
        # plt.axis('equal')    
        # plt.legend(loc='upper left')
        # ax.add_artist(centre_circle)

        # canvas_d = FigureCanvas(fig)
        # # canvas.setStyleSheet("background-color: red;")
        # # self.canvas.patch.set_facecolor('#244D54')
        # fig.patch.set_facecolor('none')
 
        # layout = QtWidgets.QVBoxLayout(self.widget_2)
        # layout.addWidget(canvas_d)