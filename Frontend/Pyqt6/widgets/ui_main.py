# from icons import icons_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6 import QtMultimedia
from PyQt5 import uic
from PyQt5.QtMultimedia import QAudioDeviceInfo,QAudio
from PyQt5.QtCore import Qt
# import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import main as Main
import keyboard

#####
input_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioInput)
output_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioOutput)

class Ui_main(object):
    test_mic = 0
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
                              "    color: #fff;\n"
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
        font.setPointSize(32)
        self.Microphone_button.setFont(font)
        self.Microphone_button.setStyleSheet("QPushButton{\n"
                                             "    background-color: rgba(0, 0, 0, 0)\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                             "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/mic.svg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Microphone_button.setIcon(icon)
        self.Microphone_button.setIconSize(QtCore.QSize(32, 32))
        self.Microphone_button.setObjectName("Microphone_button")
        self.verticalLayout.addWidget(self.Microphone_button)
        self.Audio_button = QtWidgets.QPushButton(self.Menu_button)
        self.Audio_button.setEnabled(True)

        # Audio button
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Audio_button.setFont(font)
        self.Audio_button.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgba(0, 0, 0, 0)\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/volume-2.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Audio_button.setIcon(icon1)
        self.Audio_button.setIconSize(QtCore.QSize(32, 32))
        self.Audio_button.setObjectName("Audio_button")
        self.verticalLayout.addWidget(self.Audio_button)
        self.Soundpad_button = QtWidgets.QPushButton(self.Menu_button)

        # Soundpad button
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.Soundpad_button.setFont(font)
        self.Soundpad_button.setStyleSheet("QPushButton{\n"
                                           "    background-color: rgba(0, 0, 0, 0)\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                           "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/play-circle.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Soundpad_button.setIcon(icon2)
        self.Soundpad_button.setIconSize(QtCore.QSize(32, 32))
        self.Soundpad_button.setObjectName("Soundpad_button")
        self.verticalLayout.addWidget(self.Soundpad_button)
        self.Voicechanger_button = QtWidgets.QPushButton(self.Menu_button)

        # Voicechanger button
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.Voicechanger_button.setFont(font)
        self.Voicechanger_button.setStyleSheet("QPushButton{\n"
                                               "    background-color: rgba(0, 0, 0, 0)\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                               "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/codesandbox.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Voicechanger_button.setIcon(icon3)
        self.Voicechanger_button.setIconSize(QtCore.QSize(32, 32))
        self.Voicechanger_button.setObjectName("Voicechanger_button")
        self.verticalLayout.addWidget(self.Voicechanger_button)
        self.Device_settings = QtWidgets.QFrame(self.Left_side)

        
        #Device settings
        self.Device_settings.setGeometry(QtCore.QRect(0, 330, 372, 391))

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Device_settings.sizePolicy().hasHeightForWidth())
        self.Device_settings.setSizePolicy(sizePolicy)
        self.Device_settings.setMinimumSize(QtCore.QSize(360, 330))
        self.Device_settings.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Device_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Device_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Device_settings.setObjectName("Device_settings")

#Setting Zone
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
        icon4.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/mic.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.micmute.setIcon(icon4)
        self.micmute.setIconSize(QtCore.QSize(40, 40))
        self.micmute.setObjectName("micmute")
        #เรียกใช้ฟังก์ชั่น mute mic
        self.micmute.clicked.connect(self.mic_mute)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.dropdownslider1)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(30, 110, 326, 20))
        self.horizontalSlider_2.setStyleSheet("QSlider::handle:horizontal {\n"
                                                    "border-radius: 6px;\n"
                                                    "background-color: #00d19d;;\n"
                                                "}")
        
        #กำหนดค่า max min ค่ากลาง ของ Boost mic
        self.horizontalSlider_2.setMaximum(5)
        self.horizontalSlider_2.setMinimum(-5)
        self.horizontalSlider_2.setValue(0)
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

        #เอา Virtual Cable ออกจาก List
        #โชว์ข้อมูล Input ใน dropdown
        
        self.devicesInput_list = []
        for device in input_audio_deviceInfos:
            if device.deviceName() not in self.devicesInput_list and "Virtual Cable" not in device.deviceName(): 
                self.devicesInput_list.append(device.deviceName())

        self.comboBox_2.addItems(self.devicesInput_list)
        self.comboBox_2.currentIndexChanged['QString'].connect(self.updateInput_now)
        self.comboBox_2.setCurrentIndex(0)
        
        #โชว์ข้อมูล Output ใน dropdown
        self.devicesOutput_list = []
        for device in output_audio_deviceInfos:
            if device.deviceName() not in self.devicesOutput_list and "Virtual Cable" not in device.deviceName():
                self.devicesOutput_list.append(device.deviceName())
    
        self.comboBox.addItems(self.devicesOutput_list)
        self.comboBox.currentIndexChanged['QString'].connect(self.updateOutput_now)
        self.comboBox.setCurrentIndex(0)

        ##################
        self.speakermute = QtWidgets.QPushButton(self.dropdownslider2)
        self.speakermute.setGeometry(QtCore.QRect(20, 40, 45, 45))
        self.speakermute.setMinimumSize(QtCore.QSize(45, 45))
        self.speakermute.setMaximumSize(QtCore.QSize(45, 45))
        self.speakermute.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/volume-2.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speakermute.setIcon(icon5)
        self.speakermute.setIconSize(QtCore.QSize(40, 40))
        self.speakermute.setObjectName("speakermute")
        #เรียกใช้ ฟังก์ชั่น mute volume
        self.speakermute.clicked.connect(self.volume_mute)
        self.horizontalSlider = QtWidgets.QSlider(self.dropdownslider2)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 100, 326, 20))
        self.horizontalSlider.setStyleSheet("QSlider::handle:horizontal {\n"
                                                "border-radius: 6px;\n"
                                                "background-color: #00d19d;;\n"
                                                "}")
        #set ให้ค่า current เท่ากับ value
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        current_percent = current * 100
        self.horizontalSlider.setMaximum(100)

        #set ให้โชว์ค่า value ตรง Slider bar 
        self.horizontalSlider.setValue(int(current_percent))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.updatevolume)
        self.verticalLayout_2.addWidget(self.dropdownslider2)
        self.frame = QtWidgets.QFrame(self.Device_settings)
        self.frame.setMinimumSize(QtCore.QSize(370, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.settingButton = QtWidgets.QPushButton(self.frame)
        self.settingButton.setGeometry(QtCore.QRect(30, 50, 320, 70))
        self.settingButton.setMinimumSize(QtCore.QSize(320, 70))
        self.settingButton.setMaximumSize(QtCore.QSize(320, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.settingButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/settings.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingButton.setIcon(icon6)
        self.settingButton.setIconSize(QtCore.QSize(32, 32))
        self.settingButton.setObjectName("settingButton")
        self.verticalLayout_2.addWidget(self.frame)

        #right side
        self.Right_side = QtWidgets.QFrame(ui_main)
        self.Right_side.setGeometry(QtCore.QRect(378, -1, 900, 721))
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.Right_side)

        # Microphone page size
        self.stackedWidget.setMinimumSize(QtCore.QSize(900, 720))
        self.stackedWidget.setMaximumSize(QtCore.QSize(900, 720))
        self.stackedWidget.setObjectName("stackedWidget")
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
        self.label_2 = QtWidgets.QLabel(self.Mic_title)
        self.label_2.setMinimumSize(QtCore.QSize(900, 120))
        self.label_2.setMaximumSize(QtCore.QSize(900, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.Mic_title)

        # Mic settings
        self.Noise = QtWidgets.QFrame(self.frame)
        self.Noise.setMinimumSize(QtCore.QSize(900, 190))
        self.Noise.setMaximumSize(QtCore.QSize(900, 190))
        self.Noise.setStyleSheet("QFrame{\n"
                                 "    background-color: rgba(0, 0, 0, 0);\n"
                                 "}")
        self.Noise.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Noise.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Noise.setObjectName("Noise")

        # noise button
        self.Noise_button = QtWidgets.QPushButton(self.Noise)
        self.Noise_button.setGeometry(QtCore.QRect(60, 10, 780, 170))
        self.Noise_button.setMinimumSize(QtCore.QSize(780, 170))
        self.Noise_button.setMaximumSize(QtCore.QSize(780, 170))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Noise_button.setFont(font)
        self.Noise_button.setStyleSheet("QPushButton{\n"
                                        "    background-color: #244D54;\n"
                                        "    border-style : outset;\n"
                                        "    border-width : 0.5px;\n"
                                        "    border-radius: 40px;\n"
                                        "    border-color : black;\n"
                                        "\n"
                                        "    color: rgb(104, 104, 104);\n"
                                        "    text-align : center;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(53, 112, 122);\n"
                                        "\n"
                                        "    border-width : 0.5px;\n"
                                        "    border-color :  rgb(1, 209, 158) ;\n"
                                        "    color: rgb(204, 204, 204);\n"
                                        "}\n"
                                        "")
        self.Noise_button.setObjectName("Noise_button")

        # Noice button Function
        self.Noise_button.clicked.connect(self.Noise_button_clicked)

        self.label_3 = QtWidgets.QLabel(self.Noise)
        self.label_3.setGeometry(QtCore.QRect(330, 20, 270, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                                   "\n"
                                   "    color: rgb(204, 204, 204);\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
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
                                   "    padding-left: 60px;\n"
                                   "    padding-right: 60px;\n"
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
        self.Testmic_button.setStyleSheet("QPushButton {\n"
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
                                          "}")
        self.Testmic_button.setObjectName("Testmic_button")

        # Test Mic Button Function
        self.Testmic_button.clicked.connect(self.TestMic_button_clicked)

        self.verticalLayout_5.addWidget(self.Testmic_button)
        self.verticalLayout_2.addWidget(self.TestMic)
        self.horizontalLayout_2.addWidget(self.frame)
        self.stackedWidget.addWidget(self.Microphone_page)

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
        self.Soundpad_page = QtWidgets.QWidget()
        self.Soundpad_page.setObjectName("Soundpad_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Soundpad_page)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Soundpad_label = QtWidgets.QLabel(self.Soundpad_page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Soundpad_label.setFont(font)
        self.Soundpad_label.setStyleSheet("color: #66DAED")
        self.Soundpad_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Soundpad_label.setObjectName("Soundpad_label")
        self.horizontalLayout_4.addWidget(self.Soundpad_label)
        self.stackedWidget.addWidget(self.Soundpad_page)
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


    def updateInput_now(self,value):
        print(value)
        self.device = self.devicesInput_list.index(value)
        # print('Device:',self.devicesInput_list.index(value))

    def updateOutput_now(self,value):
        print(value)
        self.device1 = self.devicesOutput_list.index(value)
        # print('Speaker:',self.devicesOutput_list.index(value))
        


    def volume_mute(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        if(Ui_main.test_mic==0):
            print("Volume Mute")
            Ui_main.test_mic=1
            volume.SetMute(1, None)
            icon_volume_mute = QtGui.QIcon()
            icon_volume_mute.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/volume-x.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_mute)
        else:
            print("Volume UnMute")
            Ui_main.test_mic=0
            volume.SetMute(0,None)
            icon_volume_unmute = QtGui.QIcon()
            icon_volume_unmute.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/volume-2.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_unmute)


    def mic_mute(self):
        if(Ui_main.test_mic==0):
            print("Mic Mute")
            Ui_main.test_mic=1
            icon_mic_mute = QtGui.QIcon()
            icon_mic_mute.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/mic-off.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.micmute.setIcon(icon_mic_mute)
        else:
            print("Mic UnMute")
            Ui_main.test_mic=0
            icon_mic_unmute = QtGui.QIcon()
            icon_mic_unmute.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/mic.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.micmute.setIcon(icon_mic_unmute)


    def updatevolume(self, value):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        try:
            volume.SetMasterVolumeLevelScalar(value / 100, None)
        except:
            print('err')
        
        if value == 0:
            icon_volume_mute = QtGui.QIcon()
            icon_volume_mute.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/volume-x.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_mute)
            volume.SetMute(1, None)
        else:
            icon_volume_unmute = QtGui.QIcon()
            icon_volume_unmute.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/volume-2.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.speakermute.setIcon(icon_volume_unmute)
            volume.SetMute(0,None)


    def updateboostmicl(self, value):
        print(value)


    def retranslateUi(self, ui_main):
        _translate = QtCore.QCoreApplication.translate
        ui_main.setWindowTitle(_translate("ui_main", "Form"))
        self.Microphone_button.setText(_translate("ui_main", "Microphone"))
        self.Audio_button.setText(_translate("ui_main", "Audio"))
        self.Soundpad_button.setText(_translate("ui_main", "Soundpad"))
        self.Voicechanger_button.setText(_translate("ui_main", "VoiceChanger"))
        self.settingButton.setText(_translate("ui_main", "Setting"))
        self.label_2.setText(_translate("ui_main", "Microphone"))
        self.Noise_button.setText(_translate("ui_main", "\n"
                                             "detecting the sound coming into the headset, and generating signals \n"
                                             "that are  out-of-phase with the  offending signals, canceling them out."))
        self.label_3.setText(_translate("ui_main", "Noise Suppression"))
        self.label.setText(_translate("ui_main", "Graph"))
        self.Testmic_button.setText(_translate("ui_main", "Test Microphone"))
        self.audio_label.setText(_translate("ui_main", "Audio"))
        self.Soundpad_label.setText(_translate("ui_main", "Soundpad"))
        self.VoiceChanger_label.setText(_translate("ui_main", "VoiceChanger"))

    def Noise_button_clicked(self):
        print("Noise button clicked")

    def TestMic_button_clicked(self):
        print("Test mic button clicked")