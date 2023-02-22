# from icons import icons_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import Qt

# IMPORT GUI FILE
from main import *
# from pages.soundpad_page import *


class Ui_mainInterface(object):
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
        font.setPointSize(28)
        self.Microphone_button.setFont(font)
        self.Microphone_button.setStyleSheet("QPushButton{\n"
                                             "    background-color: rgba(0, 0, 0, 0)\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                             "}"
                                             "QPushButton:clicked{\n"
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
        font.setPointSize(28)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Audio_button.setFont(font)
        self.Audio_button.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgba(0, 0, 0, 0)\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                        "}"
                                        "QPushButton:pressed{\n"
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
        font.setPointSize(28)
        self.Soundpad_button.setFont(font)
        self.Soundpad_button.setStyleSheet("QPushButton{\n"
                                           "    background-color: rgba(0, 0, 0, 0)\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                           "}"
                                           "QPushButton:pressed{\n"
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
        font.setPointSize(28)
        self.Voicechanger_button.setFont(font)
        self.Voicechanger_button.setStyleSheet("QPushButton{\n"
                                               "    background-color: rgba(0, 0, 0, 0)\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 218, 237, 255), stop:0.886364 rgba(31, 167, 160, 0));\n"
                                               "}"
                                               "QPushButton:pressed{\n"
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

        # Device settings
        self.Device_settings.setGeometry(QtCore.QRect(0, 329, 381, 371))
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

        # right side
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
        self.Noise_button.setGeometry(QtCore.QRect(60, 10, 780, 180))
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
                                        "    color: rgb(104, 104, 104);\n"
                                        "    text-align : center;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(53, 112, 122);    \n"
                                        "    border-width : 0.5px;\n"
                                        "    border-color :  rgb(1, 209, 158) ;\n"
                                        "    color: rgb(204, 204, 204);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: #244D54;\n"
                                        "    border-style : inset;\n"
                                        "    border-width : 2px;\n"
                                        "    border-color : #00D19D;\n"
                                        "    color: #FFFFFF;\n"
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
        self.Testmic_button.setStyleSheet("QPushButton{\n"
                                          "    background-color: #244D54;\n"
                                          "    border-style : outset;\n"
                                          "    border-width : 0.5px;\n"
                                          "    border-radius: 25px;\n"
                                          "    border-color : black;\n"
                                          "\n"
                                          "    color: rgb(104, 104, 104);\n"
                                          "    text-align : center;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(53, 112, 122);    \n"
                                          "    border-width : 0.5px;\n"
                                          "    border-color :  rgb(1, 209, 158) ;\n"
                                          "    color: rgb(204, 204, 204);\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "    background-color: #244D54;\n"
                                          "    border-style : inset;\n"
                                          "    border-width : 2px;\n"
                                          "    border-color : #00D19D;\n"
                                          "    color: #FFFFFF;\n"
                                          "}")
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

        # Soundpad Header
        self.SP_header_table = QtWidgets.QFrame(self.SP_item)
        self.SP_header_table.setMinimumSize(QtCore.QSize(900, 50))
        self.SP_header_table.setMaximumSize(QtCore.QSize(900, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SP_header_table.setFont(font)
        self.SP_header_table.setStyleSheet("QLabel\n"
                                           "{\n"
                                           "    color: #FFFFFF;\n"
                                           "}")
        self.SP_header_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_header_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_header_table.setObjectName("SP_header_table")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.SP_header_table)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # ID
        self.ID = QtWidgets.QFrame(self.SP_header_table)
        self.ID.setMinimumSize(QtCore.QSize(0, 0))
        self.ID.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.ID.setFont(font)
        self.ID.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ID.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ID.setObjectName("ID")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.ID)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.ID_label = QtWidgets.QLabel(self.ID)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ID_label.setFont(font)
        self.ID_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ID_label.setObjectName("ID_label")
        self.verticalLayout_10.addWidget(self.ID_label)
        self.horizontalLayout_6.addWidget(self.ID)

        # Name
        self.nameitem = QtWidgets.QFrame(self.SP_header_table)
        self.nameitem.setMaximumSize(QtCore.QSize(400, 50))
        self.nameitem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nameitem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nameitem.setObjectName("nameitem")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.nameitem)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.name_label = QtWidgets.QLabel(self.nameitem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("QLabel\n"
                                      "{\n"
                                      "    padding-left: 20px;\n"
                                      "}")
        self.name_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_11.addWidget(self.name_label)
        self.horizontalLayout_6.addWidget(self.nameitem)

        # Duration
        self.duraitem = QtWidgets.QFrame(self.SP_header_table)
        self.duraitem.setMaximumSize(QtCore.QSize(130, 50))
        self.duraitem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.duraitem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.duraitem.setObjectName("duraitem")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.duraitem)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.dura_rabel = QtWidgets.QLabel(self.duraitem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dura_rabel.setFont(font)
        self.dura_rabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dura_rabel.setObjectName("dura_rabel")
        self.verticalLayout_12.addWidget(self.dura_rabel)
        self.horizontalLayout_6.addWidget(self.duraitem)

        # Hotkeys
        self.hotkeysitem = QtWidgets.QFrame(self.SP_header_table)
        self.hotkeysitem.setMaximumSize(QtCore.QSize(130, 50))
        self.hotkeysitem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hotkeysitem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hotkeysitem.setObjectName("hotkeysitem")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.hotkeysitem)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.hotkeys_label = QtWidgets.QLabel(self.hotkeysitem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hotkeys_label.setFont(font)
        self.hotkeys_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hotkeys_label.setObjectName("hotkeys_label")
        self.verticalLayout_13.addWidget(self.hotkeys_label)
        self.horizontalLayout_6.addWidget(self.hotkeysitem)

        # Control
        self.controlitem = QtWidgets.QFrame(self.SP_header_table)
        self.controlitem.setMaximumSize(QtCore.QSize(200, 50))
        self.controlitem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.controlitem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controlitem.setObjectName("controlitem")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.controlitem)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.control_item = QtWidgets.QLabel(self.controlitem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.control_item.setFont(font)
        self.control_item.setAlignment(QtCore.Qt.AlignCenter)
        self.control_item.setObjectName("control_item")
        self.verticalLayout_14.addWidget(self.control_item)
        self.horizontalLayout_6.addWidget(self.controlitem)
        self.verticalLayout_8.addWidget(self.SP_header_table)

        # Soundpad Table
        self.SP_table_frame = QtWidgets.QFrame(self.SP_item)
        self.SP_table_frame.setMinimumSize(QtCore.QSize(900, 420))
        self.SP_table_frame.setMaximumSize(QtCore.QSize(900, 420))
        self.SP_table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_table_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # self.ui.tableWidget.setRowCount(3)
        # self.ui.tableWidget.setColumnCount(5)

        # self.ui.tableWidget.setColumnWidth(0, 300)
        # self.ui.tableWidget.setColumnWidth(1, 50)


        self.SP_table_frame.setObjectName("SP_table_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SP_table_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        # Soundpad Scroll Area
        self.SP_scrollArea = QtWidgets.QScrollArea(self.SP_table_frame)
        self.SP_scrollArea.setWidgetResizable(True)
        self.SP_scrollArea.setObjectName("SP_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 420))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.SP_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.SP_scrollArea)
        self.verticalLayout_8.addWidget(self.SP_table_frame)

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
        icon4.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/plus.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SP_add_button.setIcon(icon4)
        self.SP_add_button.setIconSize(QtCore.QSize(34, 34))
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

    def retranslateUi(self, ui_main):
        _translate = QtCore.QCoreApplication.translate
        ui_main.setWindowTitle(_translate("ui_main", "EchoEcho"))
        self.Microphone_button.setText(_translate("ui_main", "Microphone"))
        self.Audio_button.setText(_translate("ui_main", "Audio"))
        self.Soundpad_button.setText(_translate("ui_main", "Soundpad"))
        self.Voicechanger_button.setText(_translate("ui_main", "VoiceChanger"))
        self.Mic_title_label.setText(_translate("ui_main", "Microphone"))
        self.Noise_button.setText(_translate("ui_main", "\n"
                                             "detecting the sound coming into the headset, and generating signals \n"
                                             "that are  out-of-phase with the  offending signals, canceling them out."))
        self.Noise_label.setText(_translate("ui_main", "Noise Suppression"))
        self.label.setText(_translate("ui_main", "Graph"))
        self.Testmic_button.setText(_translate("ui_main", "Test Microphone"))
        self.audio_label.setText(_translate("ui_main", "Audio"))
        self.SP_title_label.setText(_translate("ui_main", "Soundpad"))
        self.ID_label.setText(_translate("ui_main", "NO."))
        self.name_label.setText(_translate("ui_main", "Name"))
        self.dura_rabel.setText(_translate("ui_main", "Duration"))
        self.hotkeys_label.setText(_translate("ui_main", "Hotkeys"))
        self.control_item.setText(_translate("ui_main", "Status"))
        self.VoiceChanger_label.setText(_translate("ui_main", "VoiceChanger"))

    def Noise_button_clicked(self):
        print("Noise button clicked")

    def TestMic_button_clicked(self):
        print("Test mic button clicked")

    def SP_add_item(self):
        print("SP add item")
