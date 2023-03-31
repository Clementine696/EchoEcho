# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangePages.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui_main(object):
    def setupUi(self, ui_main):
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
        self.Left_side = QtWidgets.QFrame(ui_main)
        self.Left_side.setGeometry(QtCore.QRect(-1, 0, 380, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Left_side.sizePolicy().hasHeightForWidth())
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
        self.Menubars = QtWidgets.QWidget(self.Left_side)
        self.Menubars.setGeometry(QtCore.QRect(-1, -1, 381, 330))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menubars.sizePolicy().hasHeightForWidth())
        self.Menubars.setSizePolicy(sizePolicy)
        self.Menubars.setMinimumSize(QtCore.QSize(360, 330))
        self.Menubars.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Menubars.setObjectName("Menubars")
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
        icon.addPixmap(QtGui.QPixmap(":/icons/mic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Microphone_button.setIcon(icon)
        self.Microphone_button.setIconSize(QtCore.QSize(32, 32))
        self.Microphone_button.setObjectName("Microphone_button")
        self.verticalLayout.addWidget(self.Microphone_button)
        self.Audio_button = QtWidgets.QPushButton(self.Menu_button)
        self.Audio_button.setEnabled(True)
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
        icon1.addPixmap(QtGui.QPixmap(":/icons/volume-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Audio_button.setIcon(icon1)
        self.Audio_button.setIconSize(QtCore.QSize(32, 32))
        self.Audio_button.setObjectName("Audio_button")
        self.verticalLayout.addWidget(self.Audio_button)
        self.Soundpad_button = QtWidgets.QPushButton(self.Menu_button)
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
        icon2.addPixmap(QtGui.QPixmap(":/icons/play-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Soundpad_button.setIcon(icon2)
        self.Soundpad_button.setIconSize(QtCore.QSize(32, 32))
        self.Soundpad_button.setObjectName("Soundpad_button")
        self.verticalLayout.addWidget(self.Soundpad_button)
        self.Voicechanger_button = QtWidgets.QPushButton(self.Menu_button)
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
        icon3.addPixmap(QtGui.QPixmap(":/icons/codesandbox.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Voicechanger_button.setIcon(icon3)
        self.Voicechanger_button.setIconSize(QtCore.QSize(32, 32))
        self.Voicechanger_button.setObjectName("Voicechanger_button")
        self.verticalLayout.addWidget(self.Voicechanger_button)
        self.Device_settings = QtWidgets.QFrame(self.Left_side)
        self.Device_settings.setGeometry(QtCore.QRect(0, 329, 381, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Device_settings.sizePolicy().hasHeightForWidth())
        self.Device_settings.setSizePolicy(sizePolicy)
        self.Device_settings.setMinimumSize(QtCore.QSize(360, 330))
        self.Device_settings.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Device_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Device_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Device_settings.setObjectName("Device_settings")
        self.Right_side = QtWidgets.QFrame(ui_main)
        self.Right_side.setGeometry(QtCore.QRect(380, 0, 900, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Right_side.sizePolicy().hasHeightForWidth())
        self.Right_side.setSizePolicy(sizePolicy)
        self.Right_side.setMinimumSize(QtCore.QSize(900, 700))
        self.Right_side.setMaximumSize(QtCore.QSize(900, 720))
        font = QtGui.QFont()
        font.setKerning(True)
        self.Right_side.setFont(font)
        self.Right_side.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.506091, y1:1, x2:0.501, y2:0, stop:0 rgba(74, 111, 117, 255), stop:1 rgba(98, 148, 156, 255))\n"
"}")
        self.Right_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Right_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Right_side.setObjectName("Right_side")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Right_side)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Right_side)
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
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Mic_title = QtWidgets.QFrame(self.frame)
        self.Mic_title.setMinimumSize(QtCore.QSize(900, 120))
        self.Mic_title.setMaximumSize(QtCore.QSize(900, 120))
        self.Mic_title.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.Mic_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mic_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mic_title.setObjectName("Mic_title")
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
        self.label_2.setStyleSheet("QLabel \n"
"{\n"
" color: #FFFFFF;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.Mic_title)
        self.Noise = QtWidgets.QFrame(self.frame)
        self.Noise.setMinimumSize(QtCore.QSize(900, 200))
        self.Noise.setMaximumSize(QtCore.QSize(900, 200))
        self.Noise.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.Noise.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Noise.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Noise.setObjectName("Noise")
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
"    border-style : outset;\n"
"    border-width : 2px;\n"
"    border-color : #00D19D;\n"
"    color: #FFFFFF;\n"
"}")
        self.Noise_button.setObjectName("Noise_button")
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
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.Graph)
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(170, 0, 127);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.Graph)
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
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #244D54;\n"
"    border-style : inset;\n"
"    border-width : 2px;\n"
"    border-color : #00D19D;\n"
"    color: #FFFFFF;\n"
"}")
        self.Testmic_button.setObjectName("Testmic_button")
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
        self.Alert_Frame = QtWidgets.QFrame(self.Audio_page)
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(882, 342))
        self.pushButton_2.setMaximumSize(QtCore.QSize(882, 342))
        self.pushButton_2.setObjectName("pushButton_2")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Frontend/Pyqt6/icons/alert.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(700, 300))
        self.verticalLayout_10.addWidget(self.pushButton_2)
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
        self.verticalLayout_20.setContentsMargins(50, 75, 50, 125)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label = QtWidgets.QLabel(self.Text_Frame)
        self.label.setObjectName("label")
        self.verticalLayout_20.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.Text_Frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_20.addWidget(self.pushButton)
        self.verticalLayout_19.addWidget(self.Text_Frame)
        self.horizontalLayout_3.addWidget(self.Alert_Frame)
        self.stackedWidget.addWidget(self.Audio_page)
        self.Soundpad_page = QtWidgets.QWidget()
        self.Soundpad_page.setObjectName("Soundpad_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Soundpad_page)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SP_body = QtWidgets.QFrame(self.Soundpad_page)
        self.SP_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_body.setObjectName("SP_body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.SP_body)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.SP_title = QtWidgets.QFrame(self.SP_body)
        self.SP_title.setMinimumSize(QtCore.QSize(900, 120))
        self.SP_title.setMaximumSize(QtCore.QSize(900, 120))
        self.SP_title.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.SP_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_title.setObjectName("SP_title")
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
        self.SP_item.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_item.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_item.setObjectName("SP_item")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.SP_item)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.SP_table = QtWidgets.QFrame(self.SP_item)
        self.SP_table.setMinimumSize(QtCore.QSize(900, 470))
        self.SP_table.setMaximumSize(QtCore.QSize(900, 470))
        self.SP_table.setStyleSheet("QLabel \n"
"{\n"
"    color: #000000;\n"
"}")
        self.SP_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_table.setObjectName("SP_table")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SP_table)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SP_scrollArea = QtWidgets.QScrollArea(self.SP_table)
        self.SP_scrollArea.setWidgetResizable(True)
        self.SP_scrollArea.setObjectName("SP_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 470))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(900, 470))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(900, 470))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setMinimumSize(QtCore.QSize(900, 470))
        self.tableWidget.setMaximumSize(QtCore.QSize(900, 470))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.verticalLayout_15.addWidget(self.tableWidget)
        self.SP_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.SP_scrollArea)
        self.verticalLayout_8.addWidget(self.SP_table)
        self.SP_bottom_area = QtWidgets.QFrame(self.SP_item)
        self.SP_bottom_area.setMinimumSize(QtCore.QSize(900, 130))
        self.SP_bottom_area.setMaximumSize(QtCore.QSize(900, 130))
        self.SP_bottom_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_bottom_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_bottom_area.setObjectName("SP_bottom_area")
        self.SP_add_button = QtWidgets.QPushButton(self.SP_bottom_area)
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
        icon4.addPixmap(QtGui.QPixmap(":/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SP_add_button.setIcon(icon4)
        self.SP_add_button.setIconSize(QtCore.QSize(34, 34))
        self.SP_add_button.setObjectName("SP_add_button")
        self.verticalLayout_8.addWidget(self.SP_bottom_area)
        self.verticalLayout_6.addWidget(self.SP_item)
        self.horizontalLayout_4.addWidget(self.SP_body)
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
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ui_main)

    def retranslateUi(self, ui_main):
        _translate = QtCore.QCoreApplication.translate
        ui_main.setWindowTitle(_translate("ui_main", "Form"))
        self.Microphone_button.setText(_translate("ui_main", "Microphone"))
        self.Audio_button.setText(_translate("ui_main", "Audio"))
        self.Soundpad_button.setText(_translate("ui_main", "Soundpad"))
        self.Voicechanger_button.setText(_translate("ui_main", "VoiceChanger"))
        self.label_2.setText(_translate("ui_main", "Microphone"))
        self.Noise_button.setText(_translate("ui_main", "\n"
"detecting the sound coming into the headset, and generating signals \n"
"that are  out-of-phase with the  offending signals, canceling them out."))
        self.Noise_label.setText(_translate("ui_main", "Noise Suppression"))
        self.Testmic_button.setText(_translate("ui_main", "Test Microphone"))
        # self.pushButton_2.setText(_translate("ui_main", "PushButton"))
        self.label.setWhatsThis(_translate("ui_main", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">No audio output device found</span></p></body></html>"))
        self.label.setText(_translate("ui_main", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">No audio output device found</span></p></body></html>"))
        self.pushButton.setText(_translate("ui_main", "Check your audio output device and try again"))
        self.SP_title_label.setText(_translate("ui_main", "Soundpad"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ui_main", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ui_main", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ui_main", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ui_main", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ui_main", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("ui_main", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("ui_main", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("ui_main", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("ui_main", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ui_main", "No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ui_main", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ui_main", "Duration"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ui_main", "Hotkeys"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ui_main", "Status"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.VoiceChanger_label.setText(_translate("ui_main", "VoiceChanger"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_main = QtWidgets.QWidget()
    ui = Ui_ui_main()
    ui.setupUi(ui_main)
    ui_main.show()
    sys.exit(app.exec_())
