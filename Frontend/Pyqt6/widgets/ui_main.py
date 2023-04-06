import os
import pickle

# from icons import icons_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizePolicy, QHeaderView, QAbstractItemView, QFileDialog
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioDeviceInfo, QAudio

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

# import graph file
# from newgraph import MicrophoneAudioWaveform
input_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioInput)
output_audio_deviceInfos = QAudioDeviceInfo.availableDevices(
    QAudio.AudioOutput)


class Ui_mainInterface(object):
    noise_reduce = 0
    test_microphone = 0
    VC_test_microphone = 0
    Test_VC = 0
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

        # MENUBARS
        self.Menubars = QtWidgets.QWidget(self.Left_side)
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
        self.Device_settings = QtWidgets.QFrame(self.Left_side)

        # Device settings
        self.Device_settings.setGeometry(QtCore.QRect(0, 330, 372, 391))

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
        self.setting_Button.setGeometry(QtCore.QRect(30, 50, 320, 70))
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
        self.setting_Button.setIcon(icon6)
        self.setting_Button.setIconSize(QtCore.QSize(40, 40))
        self.setting_Button.setObjectName("setting_Button")
        self.verticalLayout_2.addWidget(self.frame)

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
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.SP_title)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
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
        self.verticalLayout_7.addWidget(self.SP_title_label)
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
        self.SP_table.setMinimumSize(QtCore.QSize(900, 460))
        self.SP_table.setMaximumSize(QtCore.QSize(900, 470))
        self.SP_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_table.setObjectName("SP_table")

        # Soundpad Table Layout
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SP_table)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SP_scrollArea = QtWidgets.QScrollArea(self.SP_table)
        self.SP_scrollArea.setWidgetResizable(True)
        self.SP_scrollArea.setObjectName("SP_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 470))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
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
        self.SP_tableWidget.setColumnCount(7)
        self.SP_tableWidget.setHorizontalHeaderLabels(
            ['No.', 'Name', 'Duration', 'Hotkeys', '', 'Status', ''])
        self.SP_tableWidget.verticalHeader().hide()
        self.SP_tableWidget.horizontalHeader().setStyleSheet("QHeaderView { font-size: 10pt;"
                                                             "font-weight: bold;"
                                                             "color: #56B7C7;"
                                                             "background-color: transparent;"
                                                             "border: 0px;"
                                                             "}")

        self.SP_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.SP_tableWidget.horizontalHeader().setDisabled(True)
        self.SP_tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.SP_tableWidget.autofit = False
        self.SP_tableWidget.setColumnWidth(0, 60)
        self.SP_tableWidget.setColumnWidth(1, 400)
        self.SP_tableWidget.setColumnWidth(2, 130)
        self.SP_tableWidget.setColumnWidth(3, 110)
        self.SP_tableWidget.setColumnWidth(4, 60)
        self.SP_tableWidget.setColumnWidth(5, 60)
        self.SP_tableWidget.setColumnWidth(6, 60)

        try:
            with open("soundpad.pickle", "rb") as file:
                self.filenames = pickle.load(file)
                for fname in self.filenames:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(
                        row, 1, QTableWidgetItem(os.path.basename(fname)))
                    media_content = QMediaContent(QUrl.fromLocalFile(fname))
                    self.player.setMedia(media_content)
                    self.player.setNotifyInterval(1000)
                    self.player.mediaStatusChanged.connect(
                        lambda: self.get_duration(QMediaPlayer.LoadedMedia, fname, row))
                    self.tableWidget.setItem(
                        row, 3, QTableWidgetItem("Loading..."))
                    # self.get_duration(QMediaPlayer.LoadedMedia, fname, row)
                    self.tableWidget.setCellWidget(
                        row, 4, self.SP_listen_item("Play", fname))
                    self.tableWidget.setCellWidget(
                        row, 5, self.SP_listen_item("Listen", fname))
                    # remove_button = QPushButton("Remove")
                    # remove_button.clicked.connect(lambda _, row=row, fname=fname: self.remove_file(row, fname))
                    # self.table.setCellWidget(row, 3, remove_button)
                    remove_button = QPushButton("Delete")
                    self.tableWidget.setCellWidget(row, 6, remove_button)
                    remove_button.clicked.connect(
                        lambda _, r=row, f=fname: self.remove_file(r, f))
                print("audio load successfully")

        except Exception as e:
            print("Error loading audio files:", e)

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
        self.VC_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_frame.setObjectName("VC_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.VC_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Voice Changer Body
        self.VC_item = QtWidgets.QFrame(self.VC_frame)
        self.VC_item.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_item.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_item.setObjectName("VC_item")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.VC_item)
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName("verticalLayout_53")

        # Voice Changer Title
        self.VC_item_body = QtWidgets.QFrame(self.VC_item)
        self.VC_item_body.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.VC_item_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_item_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_item_body.setObjectName("VC_item_body")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.VC_item_body)
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.VC_title_2 = QtWidgets.QFrame(self.VC_item_body)
        self.VC_title_2.setMinimumSize(QtCore.QSize(675, 120))
        self.VC_title_2.setMaximumSize(QtCore.QSize(675, 120))
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

        # Voice Changer Table
        self.VC_table = QtWidgets.QFrame(self.VC_item_body)
        self.VC_table.setMinimumSize(QtCore.QSize(900, 600))
        self.VC_table.setMaximumSize(QtCore.QSize(900, 600))
        self.VC_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_table.setObjectName("VC_table")

        # Voice Changer Table Layout
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.VC_table)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.VC_scrollArea = QtWidgets.QScrollArea(self.VC_table)
        self.VC_scrollArea.setMinimumSize(QtCore.QSize(675, 600))
        self.VC_scrollArea.setMaximumSize(QtCore.QSize(675, 600))
        self.VC_scrollArea.setWidgetResizable(True)
        self.VC_scrollArea.setObjectName("VC_scrollArea")

        # Voice Changer Table Scroll Area
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(
            QtCore.QRect(0, 0, 675, 600))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(675, 600))
        self.scrollAreaWidgetContents_3.setMaximumSize(QtCore.QSize(675, 600))
        self.scrollAreaWidgetContents_3.setObjectName(
            "scrollAreaWidgetContents_3")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_3)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")

        # Voice Changer Table Widget
        self.VC_tableWidget = QtWidgets.QTableWidget(
            self.scrollAreaWidgetContents_3)
        # self.tableWidget_3.setMinimumSize(QtCore.QSize(675, 600))
        # self.tableWidget_3.setMaximumSize(QtCore.QSize(675, 600))
        self.VC_tableWidget.setStyleSheet("")
        self.VC_tableWidget.setObjectName("VC_tableWidget")
        self.VC_tableWidget.setColumnCount(4)
        self.VC_tableWidget.setHorizontalHeaderLabels(
            ['No.', 'Name', 'Status', ''])
        self.VC_tableWidget.verticalHeader().hide()
        self.VC_tableWidget.horizontalHeader().setStyleSheet("QHeaderView { font-size: 10pt;"
                                                             "font-weight: bold;"
                                                             "color: #56B7C7;"
                                                             "background-color: transparent;"
                                                             "border: 0px;"
                                                             "}")

        self.VC_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.VC_tableWidget.horizontalHeader().setDisabled(True)
        self.VC_tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.VC_tableWidget.autofit = False
        self.VC_tableWidget.setColumnWidth(0, 60)
        self.VC_tableWidget.setColumnWidth(1, 400)
        self.VC_tableWidget.setColumnWidth(2, 130)
        self.VC_tableWidget.setColumnWidth(3, 110)
        self.VC_tableWidget.setColumnWidth(4, 60)
        self.VC_tableWidget.setColumnWidth(5, 60)
        self.VC_tableWidget.setColumnWidth(6, 60)

        self.verticalLayout_23.addWidget(self.VC_tableWidget)
        self.VC_scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_20.addWidget(self.VC_scrollArea)
        self.verticalLayout_54.addWidget(self.VC_table)
        self.verticalLayout_53.addWidget(self.VC_item_body)

        # Test Voice Changer Button
        self.Test_VC = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Test_VC.setGeometry(QtCore.QRect(250, 440, 200, 80))
        self.Test_VC.setMinimumSize(QtCore.QSize(200, 80))
        self.Test_VC.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Test_VC.setFont(font)
        self.Test_VC.setStyleSheet("QPushButton{\n"
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
        self.Test_VC.setObjectName("Test_VC")

        # Noice button Function
        self.Test_VC.clicked.connect(self.Test_VC_clicked)

        # Voice Changer Eq Frame
        self.horizontalLayout_6.addWidget(self.VC_item)
        self.VC_Eq = QtWidgets.QFrame(self.VC_frame)
        self.VC_Eq.setMinimumSize(QtCore.QSize(225, 720))
        self.VC_Eq.setMaximumSize(QtCore.QSize(225, 720))
        self.VC_Eq.setStyleSheet("QFrame{\n"
                                 "    background-color: #324B4F\n"
                                 "}")
        self.VC_Eq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq.setObjectName("VC_Eq")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.VC_Eq)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        # Voice Changer Eq Title Frame
        self.VC_Eq_name_title = QtWidgets.QFrame(self.VC_Eq)
        self.VC_Eq_name_title.setMinimumSize(QtCore.QSize(225, 90))
        self.VC_Eq_name_title.setMaximumSize(QtCore.QSize(225, 90))
        self.VC_Eq_name_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_name_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_name_title.setObjectName("VC_Eq_name_title")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.VC_Eq_name_title)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.VC_Eq_Head = QtWidgets.QLabel(self.VC_Eq_name_title)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.VC_Eq_Head.setFont(font)
        self.VC_Eq_Head.setStyleSheet("QLabel{\n"
                                      "    color: #B0B0B0\n"
                                      "}")
        self.VC_Eq_Head.setAlignment(QtCore.Qt.AlignCenter)
        self.VC_Eq_Head.setObjectName("VC_Eq_Head")
        self.verticalLayout_12.addWidget(self.VC_Eq_Head)

        # Voice Changer Eq item name
        self.VC_name_item = QtWidgets.QLabel(self.VC_Eq_name_title)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.VC_name_item.setFont(font)
        self.VC_name_item.setStyleSheet("QLabel{\n"
                                        "    color: #FFFFFF\n"
                                        "}")
        self.VC_name_item.setAlignment(QtCore.Qt.AlignCenter)
        self.VC_name_item.setObjectName("VC_name_item")
        self.verticalLayout_12.addWidget(self.VC_name_item)
        self.verticalLayout_10.addWidget(self.VC_Eq_name_title)

        # Voice Changer Eq Setting Frame
        self.VC_Eq_setting = QtWidgets.QFrame(self.VC_Eq)
        self.VC_Eq_setting.setMinimumSize(QtCore.QSize(225, 510))
        self.VC_Eq_setting.setMaximumSize(QtCore.QSize(225, 510))
        self.VC_Eq_setting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_setting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_setting.setObjectName("VC_Eq_setting")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.VC_Eq_setting)
        self.verticalLayout_16.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")

        # Voice Changer Eq Setting 1
        self.VC_Eq_1 = QtWidgets.QFrame(self.VC_Eq_setting)
        self.VC_Eq_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_1.setObjectName("VC_Eq_1")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.VC_Eq_1)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.VC_Eq_name = QtWidgets.QFrame(self.VC_Eq_1)
        self.VC_Eq_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_name.setObjectName("VC_Eq_name")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.VC_Eq_name)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.VC_Eq_p1 = QtWidgets.QLabel(self.VC_Eq_name)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.VC_Eq_p1.setFont(font)
        self.VC_Eq_p1.setStyleSheet("QLabel{\n"
                                    "    color: #FFFFFF\n"
                                    "}")
        self.VC_Eq_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.VC_Eq_p1.setObjectName("VC_Eq_p1")
        self.verticalLayout_19.addWidget(self.VC_Eq_p1)
        self.verticalLayout_17.addWidget(self.VC_Eq_name)
        self.VC_Eq_labe_Ti = QtWidgets.QFrame(self.VC_Eq_1)
        self.VC_Eq_labe_Ti.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_labe_Ti.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_labe_Ti.setObjectName("VC_Eq_labe_Ti")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.VC_Eq_labe_Ti)
        self.horizontalLayout_7.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.VC_Eq_label_L = QtWidgets.QLabel(self.VC_Eq_labe_Ti)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_L.setFont(font)
        self.VC_Eq_label_L.setStyleSheet("QLabel{\n"
                                         "    color: #FFFFFF\n"
                                         "}")
        self.VC_Eq_label_L.setObjectName("VC_Eq_label_L")
        self.horizontalLayout_7.addWidget(self.VC_Eq_label_L)
        self.VC_Eq_label_H = QtWidgets.QLabel(self.VC_Eq_labe_Ti)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_H.setFont(font)
        self.VC_Eq_label_H.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VC_Eq_label_H.setStyleSheet("QLabel{\n"
                                         "    color: #FFFFFF\n"
                                         "}")
        self.VC_Eq_label_H.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.VC_Eq_label_H.setObjectName("VC_Eq_label_H")
        self.horizontalLayout_7.addWidget(self.VC_Eq_label_H)
        self.verticalLayout_17.addWidget(self.VC_Eq_labe_Ti)
        self.VC_slider_frame = QtWidgets.QFrame(self.VC_Eq_1)
        self.VC_slider_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_slider_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_slider_frame.setObjectName("VC_slider_frame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.VC_slider_frame)
        self.verticalLayout_18.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalSlider_VC_Eq1 = QtWidgets.QSlider(self.VC_slider_frame)
        self.horizontalSlider_VC_Eq1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_VC_Eq1.setObjectName("horizontalSlider_VC_Eq1")
        self.verticalLayout_18.addWidget(self.horizontalSlider_VC_Eq1)

        self.verticalLayout_17.addWidget(self.VC_slider_frame)
        self.verticalLayout_16.addWidget(self.VC_Eq_1)

        # Voice Changer Eq Setting 2
        self.VC_Eq_2 = QtWidgets.QFrame(self.VC_Eq_setting)
        self.VC_Eq_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_2.setObjectName("VC_Eq_2")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.VC_Eq_2)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.VC_Eq_name_6 = QtWidgets.QFrame(self.VC_Eq_2)
        self.VC_Eq_name_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_name_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_name_6.setObjectName("VC_Eq_name_6")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.VC_Eq_name_6)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.VC_Eq_p1_6 = QtWidgets.QLabel(self.VC_Eq_name_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.VC_Eq_p1_6.setFont(font)
        self.VC_Eq_p1_6.setStyleSheet("QLabel{\n"
                                      "    color: #FFFFFF\n"
                                      "}")
        self.VC_Eq_p1_6.setAlignment(QtCore.Qt.AlignCenter)
        self.VC_Eq_p1_6.setObjectName("VC_Eq_p1_6")
        self.verticalLayout_33.addWidget(self.VC_Eq_p1_6)
        self.verticalLayout_32.addWidget(self.VC_Eq_name_6)
        self.VC_Eq_labe_Ti_6 = QtWidgets.QFrame(self.VC_Eq_2)
        self.VC_Eq_labe_Ti_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_labe_Ti_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_labe_Ti_6.setObjectName("VC_Eq_labe_Ti_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.VC_Eq_labe_Ti_6)
        self.horizontalLayout_12.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.VC_Eq_label_L_6 = QtWidgets.QLabel(self.VC_Eq_labe_Ti_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_L_6.setFont(font)
        self.VC_Eq_label_L_6.setStyleSheet("QLabel{\n"
                                           "    color: #FFFFFF\n"
                                           "}")
        self.VC_Eq_label_L_6.setObjectName("VC_Eq_label_L_6")
        self.horizontalLayout_12.addWidget(self.VC_Eq_label_L_6)
        self.VC_Eq_label_H_6 = QtWidgets.QLabel(self.VC_Eq_labe_Ti_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_H_6.setFont(font)
        self.VC_Eq_label_H_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VC_Eq_label_H_6.setStyleSheet("QLabel{\n"
                                           "    color: #FFFFFF\n"
                                           "}")
        self.VC_Eq_label_H_6.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.VC_Eq_label_H_6.setObjectName("VC_Eq_label_H_6")
        self.horizontalLayout_12.addWidget(self.VC_Eq_label_H_6)
        self.verticalLayout_32.addWidget(self.VC_Eq_labe_Ti_6)
        self.VC_slider_frame_6 = QtWidgets.QFrame(self.VC_Eq_2)
        self.VC_slider_frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_slider_frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_slider_frame_6.setObjectName("VC_slider_frame_6")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.VC_slider_frame_6)
        self.verticalLayout_34.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.horizontalSlider_VC_Eq2 = QtWidgets.QSlider(self.VC_slider_frame_6)
        self.horizontalSlider_VC_Eq2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_VC_Eq2.setObjectName("horizontalSlider_VC_Eq2")
        self.verticalLayout_34.addWidget(self.horizontalSlider_VC_Eq2)
        self.verticalLayout_32.addWidget(self.VC_slider_frame_6)
        self.verticalLayout_16.addWidget(self.VC_Eq_2)

        # Voice Changer Eq Setting 5
        # self.VC_Eq_5 = QtWidgets.QFrame(self.VC_Eq_setting)
        # self.VC_Eq_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.VC_Eq_5.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.VC_Eq_5.setObjectName("VC_Eq_5")
        # self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.VC_Eq_5)
        # self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_50.setSpacing(0)
        # self.verticalLayout_50.setObjectName("verticalLayout_50")
        # self.VC_Eq_name_12 = QtWidgets.QFrame(self.VC_Eq_5)
        # self.VC_Eq_name_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.VC_Eq_name_12.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.VC_Eq_name_12.setObjectName("VC_Eq_name_12")
        # self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.VC_Eq_name_12)
        # self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_51.setSpacing(0)
        # self.verticalLayout_51.setObjectName("verticalLayout_51")
        # self.VC_Eq_p1_12 = QtWidgets.QLabel(self.VC_Eq_name_12)
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI")
        # font.setPointSize(14)
        # self.VC_Eq_p1_12.setFont(font)
        # self.VC_Eq_p1_12.setStyleSheet("QLabel{\n"
        #                                "    color: #FFFFFF\n"
        #                                "}")
        # self.VC_Eq_p1_12.setAlignment(QtCore.Qt.AlignCenter)
        # self.VC_Eq_p1_12.setObjectName("VC_Eq_p1_12")
        # self.verticalLayout_51.addWidget(self.VC_Eq_p1_12)
        # self.verticalLayout_50.addWidget(self.VC_Eq_name_12)
        # self.VC_Eq_labe_Ti_12 = QtWidgets.QFrame(self.VC_Eq_5)


        self.VC_Eq_labe_Ti_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_labe_Ti_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_labe_Ti_12.setObjectName("VC_Eq_labe_Ti_12")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.VC_Eq_labe_Ti_12)
        self.horizontalLayout_18.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.VC_Eq_label_L_12 = QtWidgets.QLabel(self.VC_Eq_labe_Ti_12)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_L_12.setFont(font)
        self.VC_Eq_label_L_12.setStyleSheet("QLabel{\n"
                                            "    color: #FFFFFF\n"
                                            "}")
        self.VC_Eq_label_L_12.setObjectName("VC_Eq_label_L_12")
        self.horizontalLayout_18.addWidget(self.VC_Eq_label_L_12)
        self.VC_Eq_label_H_12 = QtWidgets.QLabel(self.VC_Eq_labe_Ti_12)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_H_12.setFont(font)
        self.VC_Eq_label_H_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VC_Eq_label_H_12.setStyleSheet("QLabel{\n"
                                            "    color: #FFFFFF\n"
                                            "}")
        self.VC_Eq_label_H_12.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.VC_Eq_label_H_12.setObjectName("VC_Eq_label_H_12")
        self.horizontalLayout_18.addWidget(self.VC_Eq_label_H_12)
        self.verticalLayout_50.addWidget(self.VC_Eq_labe_Ti_12)
        self.VC_slider_frame_12 = QtWidgets.QFrame(self.VC_Eq_5)
        self.VC_slider_frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_slider_frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_slider_frame_12.setObjectName("VC_slider_frame_12")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.VC_slider_frame_12)
        self.verticalLayout_52.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.horizontalSlider_VC_Eq3 = QtWidgets.QSlider(self.VC_slider_frame_12)
        self.horizontalSlider_VC_Eq3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_VC_Eq3.setObjectName("horizontalSlider_VC_Eq3")
        self.verticalLayout_52.addWidget(self.horizontalSlider_VC_Eq3)
        self.verticalLayout_50.addWidget(self.VC_slider_frame_12)
        self.verticalLayout_16.addWidget(self.VC_Eq_5)

        # Voice Changer Eq Setting 3
        self.VC_Eq_3 = QtWidgets.QFrame(self.VC_Eq_setting)
        self.VC_Eq_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_3.setObjectName("VC_Eq_3")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.VC_Eq_3)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.VC_Eq_name_8 = QtWidgets.QFrame(self.VC_Eq_3)
        self.VC_Eq_name_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_name_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_name_8.setObjectName("VC_Eq_name_8")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.VC_Eq_name_8)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.VC_Eq_p1_8 = QtWidgets.QLabel(self.VC_Eq_name_8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.VC_Eq_p1_8.setFont(font)
        self.VC_Eq_p1_8.setStyleSheet("QLabel{\n"
                                      "    color: #FFFFFF\n"
                                      "}")
        self.VC_Eq_p1_8.setAlignment(QtCore.Qt.AlignCenter)
        self.VC_Eq_p1_8.setObjectName("VC_Eq_p1_8")
        self.verticalLayout_39.addWidget(self.VC_Eq_p1_8)
        self.verticalLayout_38.addWidget(self.VC_Eq_name_8)
        self.VC_Eq_labe_Ti_8 = QtWidgets.QFrame(self.VC_Eq_3)
        self.VC_Eq_labe_Ti_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_labe_Ti_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_labe_Ti_8.setObjectName("VC_Eq_labe_Ti_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.VC_Eq_labe_Ti_8)
        self.horizontalLayout_14.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.VC_Eq_label_L_8 = QtWidgets.QLabel(self.VC_Eq_labe_Ti_8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_L_8.setFont(font)
        self.VC_Eq_label_L_8.setStyleSheet("QLabel{\n"
                                           "    color: #FFFFFF\n"
                                           "}")
        self.VC_Eq_label_L_8.setObjectName("VC_Eq_label_L_8")
        self.horizontalLayout_14.addWidget(self.VC_Eq_label_L_8)
        self.VC_Eq_label_H_8 = QtWidgets.QLabel(self.VC_Eq_labe_Ti_8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_H_8.setFont(font)
        self.VC_Eq_label_H_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VC_Eq_label_H_8.setStyleSheet("QLabel{\n"
                                           "    color: #FFFFFF\n"
                                           "}")
        self.VC_Eq_label_H_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.VC_Eq_label_H_8.setObjectName("VC_Eq_label_H_8")
        self.horizontalLayout_14.addWidget(self.VC_Eq_label_H_8)
        self.verticalLayout_38.addWidget(self.VC_Eq_labe_Ti_8)
        self.VC_slider_frame_8 = QtWidgets.QFrame(self.VC_Eq_3)
        self.VC_slider_frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_slider_frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_slider_frame_8.setObjectName("VC_slider_frame_8")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.VC_slider_frame_8)
        self.verticalLayout_40.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.horizontalSlider_VC_Eq4 = QtWidgets.QSlider(self.VC_slider_frame_8)
        self.horizontalSlider_VC_Eq4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_VC_Eq4.setObjectName("horizontalSlider_VC_Eq4")
        self.verticalLayout_40.addWidget(self.horizontalSlider_VC_Eq4)
        self.verticalLayout_38.addWidget(self.VC_slider_frame_8)
        self.verticalLayout_16.addWidget(self.VC_Eq_3)

        # Voice Changer Eq Setting 5
        self.VC_Eq_5 = QtWidgets.QFrame(self.VC_Eq_setting)
        self.VC_Eq_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_5.setObjectName("VC_Eq_5")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.VC_Eq_5)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.VC_Eq_name_9 = QtWidgets.QFrame(self.VC_Eq_5)
        self.VC_Eq_name_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_name_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_name_9.setObjectName("VC_Eq_name_9")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.VC_Eq_name_9)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.VC_Eq_p1_9 = QtWidgets.QLabel(self.VC_Eq_name_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.VC_Eq_p1_9.setFont(font)
        self.VC_Eq_p1_9.setStyleSheet("QLabel{\n"
                                      "    color: #FFFFFF\n"
                                      "}")
        self.VC_Eq_p1_9.setAlignment(QtCore.Qt.AlignCenter)
        self.VC_Eq_p1_9.setObjectName("VC_Eq_p1_9")
        self.verticalLayout_42.addWidget(self.VC_Eq_p1_9)
        self.verticalLayout_41.addWidget(self.VC_Eq_name_9)
        self.VC_Eq_labe_Ti_9 = QtWidgets.QFrame(self.VC_Eq_5)
        self.VC_Eq_labe_Ti_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_labe_Ti_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_labe_Ti_9.setObjectName("VC_Eq_labe_Ti_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.VC_Eq_labe_Ti_9)
        self.horizontalLayout_15.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.VC_Eq_label_L_9 = QtWidgets.QLabel(self.VC_Eq_labe_Ti_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_L_9.setFont(font)
        self.VC_Eq_label_L_9.setStyleSheet("QLabel{\n"
                                           "    color: #FFFFFF\n"
                                           "}")
        self.VC_Eq_label_L_9.setObjectName("VC_Eq_label_L_9")
        self.horizontalLayout_15.addWidget(self.VC_Eq_label_L_9)
        self.VC_Eq_label_H_9 = QtWidgets.QLabel(self.VC_Eq_labe_Ti_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.VC_Eq_label_H_9.setFont(font)
        self.VC_Eq_label_H_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VC_Eq_label_H_9.setStyleSheet("QLabel{\n"
                                           "    color: #FFFFFF\n"
                                           "}")
        self.VC_Eq_label_H_9.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.VC_Eq_label_H_9.setObjectName("VC_Eq_label_H_9")
        self.horizontalLayout_15.addWidget(self.VC_Eq_label_H_9)
        self.verticalLayout_41.addWidget(self.VC_Eq_labe_Ti_9)
        self.VC_slider_frame_9 = QtWidgets.QFrame(self.VC_Eq_5)
        self.VC_slider_frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_slider_frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_slider_frame_9.setObjectName("VC_slider_frame_9")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.VC_slider_frame_9)
        self.verticalLayout_43.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.horizontalSlider_VC_Eq5 = QtWidgets.QSlider(self.VC_slider_frame_9)
        self.horizontalSlider_VC_Eq5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_VC_Eq5.setObjectName("horizontalSlider_VC_Eq5")
        self.verticalLayout_43.addWidget(self.horizontalSlider_VC_Eq5)
        self.verticalLayout_41.addWidget(self.VC_slider_frame_9)
        self.verticalLayout_16.addWidget(self.VC_Eq_5)
        self.verticalLayout_10.addWidget(self.VC_Eq_setting)
        self.VC_Eq_button = QtWidgets.QFrame(self.VC_Eq)
        self.VC_Eq_button.setMaximumSize(QtCore.QSize(225, 110))
        self.VC_Eq_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VC_Eq_button.setStyleSheet("QFrame{\n"
                                        "    padding-left: 12.5px;\n"
                                        "}")
        self.VC_Eq_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VC_Eq_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VC_Eq_button.setObjectName("VC_Eq_button")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.VC_Eq_button)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")

        # VC_Eq_button
        self.VC_Testmic_button = QtWidgets.QPushButton(self.VC_Eq_button)
        self.VC_Testmic_button.setMinimumSize(QtCore.QSize(200, 80))
        self.VC_Testmic_button.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.VC_Testmic_button.setFont(font)
        self.VC_Testmic_button.setStyleSheet("QPushButton{\n"
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
        self.VC_Testmic_button.setObjectName("VC_Testmic_button")

        # Test Mic Button Function
        self.VC_Testmic_button.clicked.connect(self.VC_Testmic_button_clicked)

        self.verticalLayout_14.addWidget(self.VC_Testmic_button)
        self.verticalLayout_10.addWidget(self.VC_Eq_button)
        self.horizontalLayout_6.addWidget(self.VC_Eq)
        self.horizontalLayout_5.addWidget(self.VC_frame)
        self.stackedWidget.addWidget(self.Voicechanger_page)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(ui_main)
        self.stackedWidget.setCurrentIndex(3)
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

        self.VC_title_label_2.setText(_translate("ui_main", "Voice Changer"))

        ####
        self.Test_VC.setText(_translate("ui_main", "Test item 1"))
        ####

        self.VC_Eq_Head.setText(_translate("ui_main", "Voice configuration"))
        self.VC_name_item.setText(_translate("ui_main", "Alien"))
        self.VC_Eq_p1.setText(_translate("ui_main", "Pitch Shift Factor"))
        self.VC_Eq_label_L.setText(_translate("ui_main", "Low"))
        self.VC_Eq_label_H.setText(_translate("ui_main", "High"))
        self.VC_Eq_p1_6.setText(_translate("ui_main", "Bins"))
        self.VC_Eq_label_L_6.setText(_translate("ui_main", "Low"))
        self.VC_Eq_label_H_6.setText(_translate("ui_main", "High"))
        self.VC_Eq_p1_12.setText(_translate("ui_main", "Hz"))
        self.VC_Eq_label_L_12.setText(_translate("ui_main", "Low"))
        self.VC_Eq_label_H_12.setText(_translate("ui_main", "High"))
        # self.VC_Eq_p1_8.setText(_translate("ui_main", "???"))
        # self.VC_Eq_label_L_8.setText(_translate("ui_main", "Low"))
        # self.VC_Eq_label_H_8.setText(_translate("ui_main", "High"))
        # self.VC_Eq_p1_9.setText(_translate("ui_main", "???"))
        # self.VC_Eq_label_L_9.setText(_translate("ui_main", "Low"))
        # self.VC_Eq_label_H_9.setText(_translate("ui_main", "High"))
        self.VC_Testmic_button.setText(
            _translate("ui_main", "Test Microphone"))

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
        print("SP add item")
        options = QFileDialog.Options()
        folder = r""
        # เห็นเฉพาะ .wav, .mp3
        fname, _ = QFileDialog.getOpenFileName(
            self.ui_main, "QFileDialog.getOpenFileName()", folder, "WAV Files (*.wav);; MP3 Files (*.mp3)", options=options)
        if fname:
            print("add file :", fname)
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(
                row, 1, QTableWidgetItem(os.path.basename(fname)))
            # self.table.setItem(row, 1, QTableWidgetItem(""))
            # self.get_duration(QMediaPlayer.LoadedMedia, fname, row)
            media_content = QMediaContent(QUrl.fromLocalFile(fname))
            self.player.setMedia(media_content)
            self.player.setNotifyInterval(1000)
            self.player.mediaStatusChanged.connect(
                lambda: self.get_duration(QMediaPlayer.LoadedMedia, fname, row))
            self.tableWidget.setItem(row, 3, QTableWidgetItem("Loading..."))
            self.tableWidget.setCellWidget(
                row, 4, self.SP_listen_item("Play", fname))
            self.tableWidget.setCellWidget(
                row, 5, self.SP_listen_item("Listen", fname))
            remove_button = QPushButton("Delete")
            remove_button.clicked.connect(
                lambda _, row=row, fname=fname: self.remove_file(row, fname))
            self.tableWidget.setCellWidget(row, 6, remove_button)
            self.filenames.append(fname)
            self.save_file()

    # play item
    def SP_play_item(self, row):
        print("SP play item", row)

    # listen item button
    def SP_listen_item(self, text, filename):
        button = QPushButton(text)
        button.clicked.connect(lambda: self.play_media(
            filename, self.tableWidget.currentRow()))
        return button

    def play_media(self, filename, row):
        fname = filename
        # convert string to QUrl object using the QUrl constructor
        file = QUrl.fromLocalFile(fname)
        media = QMediaContent(file)
        self.player.setMedia(media)
        # play the media
        self.player.play()
        # self.player.mediaStatusChanged.connect(lambda status: self.get_duration(status, filename, row))

    def get_duration(self, media_status, fname, row):
        if media_status == QMediaPlayer.LoadedMedia:
            duration = self.player.duration() / 1000.0
            self.tableWidget.setItem(
                row, 2, QTableWidgetItem("{:.2f} s".format(duration)))

    # delete item button
    def SP_del_item(self, row, fname):
        button = QPushButton("Delete")
        button.clicked.connect(lambda: self.remove_file(row, fname))
        return button

    def remove_file(self, row, fname):
        # Remove the selected row from the table
        if fname in self.filenames:
            self.filenames.remove(fname)
        self.tableWidget.removeRow(row)
        # os.remove()

        # self.filenames.remove(fname)
        # self.table.removeRow(row)

        # Save the updated list of filenames
        self.save_file()

        # Stop the player if it was playing the removed file
        if self.player.state() == QMediaPlayer.PlayingState and self.player.currentMedia().canonicalUrl().toLocalFile() == fname:
            self.player.stop()

        print("File removed successfully.")

    def save_file(self):
        # save file in pickle
        with open("soundpad.pickle", "wb") as file:
            pickle.dump(self.filenames, file)

    #########################################################
    # Voice Changer Page Function
    def Test_VC_clicked(self):
        print("Test VC clicked")
        if (Ui_mainInterface.Test_VC == 0):
            Ui_mainInterface.Test_VC = 1
            # ทำให้ปุ่มเปิด
            self.Test_VC.setStyleSheet("QPushButton{\n"
                                              "    border-radius: 25px;\n"
                                              "    background-color: #244D54;\n"
                                              "    border-style : inset;\n"
                                              "    border-width : 2px;\n"
                                              "    border-color : #00D19D;\n"
                                              "    color: #FFFFFF;\n"
                                              "}"
                                              )
        else:
            Ui_mainInterface.Test_VC = 0
            # ทำปุ่มปิด
            self.Test_VC.setStyleSheet("QPushButton{\n"
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

    def VC_Testmic_button_clicked(self):
        print("VC Test mic button clicked")
        if (Ui_mainInterface.VC_test_microphone == 0):
            Ui_mainInterface.VC_test_microphone = 1
            # ทำให้ปุ่มเปิด
            self.VC_Testmic_button.setStyleSheet("QPushButton{\n"
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
            self.VC_Testmic_button.setStyleSheet("QPushButton{\n"
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
