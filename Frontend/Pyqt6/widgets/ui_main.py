import os
import pickle
import time

# from icons import icons_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizePolicy, QHeaderView, QAbstractItemView, QFileDialog
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioDeviceInfo, QAudio

from mutagen.mp3 import MP3
from mutagen.wave import WAVE

# IMPORT GUI FILE
from main import *
# from pages.soundpad_page import *
# from PySide6 import QtMultimedia
from PyQt5 import uic
# import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import main as Main
import keyboard
import subprocess


#import graph file
from newgraph import MicrophoneAudioWaveform
input_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioInput)
output_audio_deviceInfos = QAudioDeviceInfo.availableDevices(
    QAudio.AudioOutput)


class Ui_mainInterface(object):
    noise_reduce = 0
    test_microphone = 0
    microphone_mute = 0
    audio_mute = 0
    Mic_Side_menu = 0
    SP_Side_menu = 0
    VC_Side_menu = 0

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
        self.Microphone_button = QtWidgets.QPushButton(self.Menu_button)
        self.Microphone_button.setEnabled(True)

        # Microphone button
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
        self.framedefault.setGeometry(QtCore.QRect(0, 100, 371, 221))
        self.framedefault.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framedefault.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framedefault.setObjectName("framedefault")
        self.detaildefault = QtWidgets.QTextEdit(self.framedefault)
        self.detaildefault.setGeometry(QtCore.QRect(30, 10, 321, 111))
        self.detaildefault.setObjectName("detaildefault")
        self.settodefault = QtWidgets.QPushButton(self.framedefault)
        self.settodefault.setGeometry(QtCore.QRect(30, 140, 320, 54))
        self.settodefault.setMinimumSize(QtCore.QSize(320, 54))
        self.settodefault.setMaximumSize(QtCore.QSize(320, 54))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.settodefault.setFont(font)
        self.settodefault.setStyleSheet("QPushButton { \n"
"    background-color: #850021;\n"
"    color: #ffffff;\n"
"}")
        self.settodefault.setObjectName("settodefault")
        self.frameEquipment = QtWidgets.QFrame(self.page_6)
        self.frameEquipment.setGeometry(QtCore.QRect(0, 320, 371, 151))
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
        # self.graph = MicrophoneAudioWaveform()

        self.label = QtWidgets.QLabel(self.Graph)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
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

        # Audio Page
        self.Audio_page = QtWidgets.QWidget()
        self.Audio_page.setObjectName("Audio_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Audio_page)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.audio_label = QtWidgets.QLabel(self.Audio_page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.audio_label.setFont(font)
        self.audio_label.setStyleSheet("color: #66DAED")
        self.audio_label.setAlignment(QtCore.Qt.AlignCenter)
        self.audio_label.setObjectName("audio_label")
        self.horizontalLayout_3.addWidget(self.audio_label)
        self.stackedWidget.addWidget(self.Audio_page)

        #Dashbord Page
        self.dashbord_page = QtWidgets.QWidget()
        self.dashbord_page.setObjectName("dashbord")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.dashbord_page)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dashbord_label = QtWidgets.QLabel(self.Audio_page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.dashbord_label.setFont(font)
        self.dashbord_label.setStyleSheet("color: #66DAED")
        self.dashbord_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dashbord_label.setObjectName("dashbord_label")
        self.horizontalLayout_6.addWidget(self.dashbord_label)
        self.stackedWidget.addWidget(self.dashbord_page)

        # Soundpad Page
        self.filenames = []
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
        self.pushButton = QtWidgets.QPushButton(self.SP_title)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        # self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        icon_dash = QtGui.QIcon()
        icon_dash.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/icons8-combo-chart-96.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # DAshboad button clicked
        # self.pushButton.clicked.connect()

        self.pushButton.setIcon(icon_dash)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout_6.addWidget(self.pushButton)
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
        self.SP_table.setMinimumSize(QtCore.QSize(880, 460))
        self.SP_table.setMaximumSize(QtCore.QSize(880, 470))
        self.SP_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_table.setObjectName("SP_table")

        #
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 880, 470))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.SP_scrollArea.horizontalScrollBar().hide()
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.tableWidget = QtWidgets.QTableWidget(
            self.scrollAreaWidgetContents)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(5)
        # self.tableWidget.setRowCount(9)

        # self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ['No.', 'Name', 'Duration', 'Hotkeys', '', 'Status', ''])
        self.tableWidget.verticalHeader().hide()
        # effect = QGraphicsDropShadowEffect()
        # self.tableWidget.setGraphicsEffect(effect)
        # self.tableWidget.setStyleSheet("QHeaderView {\n"
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
        self.tableWidget.setStyleSheet("QTableWidget::item {"
                                                          "color: #d7d7d7;"
                                                          "background-color: rgba(50, 75, 79, 140)"
                                                        #   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(138, 138, 138, 50), stop:0.886364 rgba(102, 218, 237, 255));"
                                                          "}"
                                        "QTableWidget{"
                                                          "gridline-color:  transparent;"
                                                          "}"
                                                          )
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section { font-size: 10pt;"
                                                          "font-weight: bold;"
                                                          "color: #56B7C7;"
                                                          "background-color: transparent;"
                                                          "}"
                                                          "QHeaderView {"
                                                          "border-bottom: 1px solid #00FFF0;"
                                                          "}")

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setDisabled(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.tableWidget.autofit = False
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 110)
        self.tableWidget.setColumnWidth(4, 60)
        self.tableWidget.setColumnWidth(5, 60)
        self.tableWidget.setColumnWidth(6, 60)

        try:
            with open("soundpad.pickle", "rb") as file:
                self.filenames = pickle.load(file)
                for fname in self.filenames:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(os.path.basename(fname)))

                    duration = self.getDuration(fname)
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(duration))   

                    self.tableWidget.setCellWidget(row, 4, self.play_button("Play", fname))

                    self.tableWidget.setCellWidget(row, 5, self.listen_button("Listen", fname))

                    remove_button = self.remove_button(row, fname)

                    self.tableWidget.setCellWidget(row, 6, remove_button)
                    remove_button.clicked.connect(lambda _, r=row, f=fname: self.remove_file(r, f))

                print("audio load successfully")

        except Exception as e:
            print("Error loading audio files:",e)

        # for index in range(self.tableWidget.rowCount()):

        #     # play button
        #     self.btn_play = QPushButton(self.tableWidget)
        #     self.btn_play.setText('Play')
        #     self.tableWidget.setCellWidget(index, 4, self.btn_play)
        #     self.btn_play.clicked.connect(
        #         lambda: self.SP_play_item(self.tableWidget.currentRow()))

        #     # listen button
        #     self.btn_listen = QPushButton(self.tableWidget)
        #     self.btn_listen.setText('Listen')
        #     self.tableWidget.setCellWidget(index, 5, self.btn_listen)
        #     self.btn_listen.clicked.connect(
        #         lambda: self.SP_listen_item(self.tableWidget.currentRow()))

        #     # delete button
        #     self.btn_delete = QPushButton(self.tableWidget)
        #     self.btn_delete.setText('delete')
        #     self.tableWidget.setCellWidget(index, 6, self.btn_delete)
        #     self.btn_delete.clicked.connect(
        #         lambda: self.remove_file(self.tableWidget.currentRow()))

        self.verticalLayout_15.addWidget(self.tableWidget)
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
        self.Voicechanger_page.setObjectName("Voicechanger_page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Voicechanger_page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.VoiceChanger_label = QtWidgets.QLabel(self.Voicechanger_page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.VoiceChanger_label.setFont(font)
        self.VoiceChanger_label.setStyleSheet("color: #66DAED")
        self.VoiceChanger_label.setAlignment(QtCore.Qt.AlignCenter)
        self.VoiceChanger_label.setObjectName("VoiceChanger_label")
        self.horizontalLayout_5.addWidget(self.VoiceChanger_label)
        self.stackedWidget.addWidget(self.Voicechanger_page)
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
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        return cast(interface, POINTER(IAudioEndpointVolume))
    
    def open_device(self):
        subprocess.run(["control", "mmsys.cpl"])

    
    def updatevolume(self,value):
        self.volume.SetMasterVolumeLevelScalar(self.horizontalSlider.value() / 100, None)
        if value == 0:
            Ui_mainInterface.audio_mute = 1
            icon_volume_mute = QtGui.QIcon()
            icon_volume_mute.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/mutespeaker-sai8.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_mute)
            self.volume.SetMute(1, None)
        else:
            Ui_mainInterface.audio_mute = 0
            icon_volume_unmute = QtGui.QIcon()
            icon_volume_unmute.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/unmutespeaker-sai8.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_unmute)
            self.volume.SetMute(0,None)

    def retranslateUi(self, ui_main):
        _translate = QtCore.QCoreApplication.translate
        ui_main.setWindowTitle(_translate("ui_main", "EchoEcho"))
        self.Microphone_button.setText(_translate("ui_main", "Microphone"))
        self.Soundpad_button.setText(_translate("ui_main", "Soundpad"))
        self.Voicechanger_button.setText(_translate("ui_main", "VoiceChanger"))
        self.Mic_title_label.setText(_translate("ui_main", "Microphone"))
        self.setting_Button.setText(_translate("ui_main", "Setting"))
        self.Noise_button.setText(_translate("ui_main", "\n"
                                             "detecting the sound coming into the headset, and generating signals \n"
                                             "that are  out-of-phase with the  offending signals, canceling them out."))
        self.Noise_label.setText(_translate("ui_main", "Noise Suppression"))
        self.label.setText(_translate("ui_main", "Graph_text"))
        self.Testmic_button.setText(_translate("ui_main", "Test Microphone"))
        self.audio_label.setText(_translate("ui_main", "Audio"))
        self.SP_title_label.setText(_translate("ui_main", "Soundpad"))
        self.dashbord_label.setText(_translate("ui_main", "Dashbord"))

        self.VoiceChanger_label.setText(_translate("ui_main", "VoiceChanger"))
        self.settingmain.setText(_translate("ui_main", "Settings"))
        self.detaildefault.setHtml(_translate("ui_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#cccccc;\">Remove optimization from digital devices currently set as default. This will restore their original configurations.</span></p></body></html>"))
        self.settodefault.setText(_translate("ui_main", "set to default"))
        self.detailequipment.setHtml(_translate("ui_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#cccccc;\">Open control panel sound card setting.</span></p></body></html>"))
        self.Equipmentsetting.setText(_translate("ui_main", "Equipment setting"))
        self.Tutorial.setText(_translate("ui_main", "Tutorial"))
        self.settingButton.setText(_translate("ui_main", "Setting"))

    # Side menu button clicked
    ##############################
    def Mic_Side_menu_clicked(self):
        # Mic clciked
        ##############################
        if (Ui_mainInterface.Mic_Side_menu == 0):
            print("MIC clicked")
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
            print("SP clicked")
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
            print("VC clicked")
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
        else:
            Ui_mainInterface.noise_reduce = 0
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

    def SP_add_item(self):
        options = QFileDialog.Options()
        folder = r""

        fname, _ = QFileDialog.getOpenFileName(self.ui_main, "QFileDialog.getOpenFileName()", folder, "WAV Files (*.wav);; MP3 Files (*.mp3)", options=options)
        if fname:
            print("add file :", fname)

            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(os.path.basename(fname)))
            # self.table.setItem(row, 1, QTableWidgetItem(""))
            # self.get_duration(QMediaPlayer.LoadedMedia, fname, row)

            duration = self.getDuration(fname)
            self.tableWidget.setItem(row, 2, QTableWidgetItem(duration)) 
 
            self.tableWidget.setCellWidget(row, 4, self.play_button("", fname))

            self.tableWidget.setCellWidget(row, 5, self.listen_button("", fname))

            remove_button = self.remove_button(row, fname)

            self.tableWidget.setCellWidget(row, 6, remove_button)
            remove_button.clicked.connect(lambda _, r=row, f=fname: self.remove_file(r, f))
            self.save_file()

    # play item

    # ========================================================================================================================================
    def play_mic(self, row, filename):
        fname = filename
        # convert string to QUrl object using the QUrl constructor
        file = QUrl.fromLocalFile(fname)
        media = QMediaContent(file)
        self.player.setMedia(media)
        # play the media
        self.player.play()

    def play_button(self, label, fname):
        icon_play = QtGui.QIcon()
        icon_play.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/icons8-play-button-circled-48.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        play_button = QPushButton(label)
        play_button.setIcon(icon_play)
        play_button.clicked.connect(lambda: self.play_media(play_button, fname))
        return play_button

    def play_media(self, btn, fname):
        icon_pause = QtGui.QIcon()
        icon_pause.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/icons8-pause-button-48.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_play = QtGui.QIcon()
        icon_play.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/icons8-play-button-circled-48.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        media_content = QMediaContent(QUrl.fromLocalFile(fname))
        if self.player.state() == QMediaPlayer.PlayingState and self.player.media().canonicalUrl() == media_content.canonicalUrl():
            self.player.stop()
            # play_button
            btn.setIcon(icon_play)
            # btn.setText("play")
        else:
            if self.player.state() == QMediaPlayer.PlayingState:
                curr_fname = self.player.currentMedia().canonicalUrl().toLocalFile()
                curr_btn = self.get_play(curr_fname)
                if curr_btn is not None:
                    curr_btn.setIcon(icon_play)
                    # curr_btn.setText("Play")
                self.player.stop()

            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 1)
                if item is not None and item.text() != os.path.basename(fname):
                    play_btn = self.tableWidget.cellWidget(row, 4)
                    if play_btn.setIcon(icon_pause) == btn.setIcon(icon_pause):
                        self.player.stop()
                        play_btn.setIcon(icon_play)
                        # play_btn.setText("Play")

            self.player.setMedia(media_content)
            self.player.play()
            btn.setIcon(icon_pause)
            # btn.setText("Stop")


    def get_play(self, fname):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item is not None and item.text() == os.path.basename(fname):
                return self.tableWidget.cellWidget(row, 4)
            
    # ========================================================================================================================================
            
    def listen_button(self, label, fname):
        icon_listen = QtGui.QIcon()
        icon_listen.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/icons8-headphone-48.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        listen_button = QPushButton(label)
        listen_button.setIcon(icon_listen)
        listen_button.clicked.connect(lambda: self.listen_media(listen_button, fname))
        return listen_button

    def listen_media(self, btn, fname):
        icon_listen = QtGui.QIcon()
        icon_listen.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/icons8-headphone-48.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_pause = QtGui.QIcon()
        icon_pause.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/icons8-pause-button-48.png"),
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

            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 1)
                if item is not None and item.text() != os.path.basename(fname):
                    play_btn = self.tableWidget.cellWidget(row, 5)
                    if play_btn.setIcon(icon_pause) == btn.setIcon(icon_pause):
                        self.player.stop()
                        play_btn.setIcon(icon_listen)
                        # play_btn.setText("")

            self.player.setMedia(media_content)
            self.player.play()
            btn.setIcon(icon_pause)
            # btn.setText("")

    def get_listen(self, fname):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item is not None and item.text() == os.path.basename(fname):
                return self.tableWidget.cellWidget(row, 5)

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
        icon_remove.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/icons8-trash-can-48.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        remove_button = QPushButton()
        remove_button.setIcon(icon_remove)
        remove_button.clicked.connect(lambda: self.remove_file(row, fname))
        return remove_button

    def remove_file(self, row, fname):
        if fname in self.filenames:
            self.filenames.remove(fname)
        self.tableWidget.removeRow(row)
        
        self.save_file()

        # Stop the player if it was playing the removed file
        if self.player.state() == QMediaPlayer.PlayingState and self.player.currentMedia().canonicalUrl().toLocalFile() == fname:
            self.player.stop()

        print("File removed successfully.")

    def save_file(self):
        # save file in pickle
        with open("soundpad.pickle", "wb") as file:
            pickle.dump(self.filenames, file)