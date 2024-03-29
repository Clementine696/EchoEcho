from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Microphone_page(object):
    def setupUi(self, Microphone_page):
        Microphone_page.setObjectName("Microphone_page")
        Microphone_page.resize(900, 680)
        Microphone_page.setMinimumSize(QtCore.QSize(900, 680))
        Microphone_page.setMaximumSize(QtCore.QSize(900, 680))
        Microphone_page.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Microphone_page)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Microphone_page)
        self.frame.setMinimumSize(QtCore.QSize(900, 680))
        self.frame.setMaximumSize(QtCore.QSize(900, 680))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.506091, y1:0, x2:0.506, y2:1, stop:0 rgba(74, 111, 117, 255), stop:1 rgba(98, 148, 156, 255));\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Mic_title = QtWidgets.QFrame(self.frame)
        self.Mic_title.setMinimumSize(QtCore.QSize(900, 120))
        self.Mic_title.setMaximumSize(QtCore.QSize(900, 120))
        self.Mic_title.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0)\n"
"}")
        self.Mic_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mic_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mic_title.setObjectName("Mic_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Mic_title)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Label_head = QtWidgets.QLabel(self.Mic_title)
        self.Label_head.setMinimumSize(QtCore.QSize(900, 120))
        self.Label_head.setMaximumSize(QtCore.QSize(900, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.Label_head.setFont(font)
        self.Label_head.setStyleSheet("QLabel\n"
"{\n"
"    color: #FFFFFF\n"
"\n"
"}")
        self.Label_head.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_head.setObjectName("Label_head")
        self.verticalLayout_2.addWidget(self.Label_head)
        self.verticalLayout.addWidget(self.Mic_title)
        self.M_button = QtWidgets.QFrame(self.frame)
        self.M_button.setMinimumSize(QtCore.QSize(900, 190))
        self.M_button.setMaximumSize(QtCore.QSize(900, 190))
        self.M_button.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.M_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.M_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.M_button.setObjectName("M_button")
        self.noise_button = QtWidgets.QPushButton(self.M_button)
        self.noise_button.setGeometry(QtCore.QRect(60, 10, 780, 170))
        self.noise_button.setMinimumSize(QtCore.QSize(780, 170))
        self.noise_button.setMaximumSize(QtCore.QSize(780, 170))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.noise_button.setFont(font)
        self.noise_button.setStyleSheet("QPushButton{\n"
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
        self.noise_button.setObjectName("noise_button")
        self.label = QtWidgets.QLabel(self.M_button)
        self.label.setGeometry(QtCore.QRect(320, 20, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"    color: rgb(204, 204, 204);\n"
"\n"
"    \n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.M_button)
        self.Graph = QtWidgets.QFrame(self.frame)
        self.Graph.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0)\n"
"}")
        self.Graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph.setObjectName("Graph")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Graph)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.Graph)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(900, 120))
        self.frame_2.setMaximumSize(QtCore.QSize(900, 120))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"\n"
"    padding-left: 60px;\n"
"    padding-right: 60px;\n"
"    padding-top: 0px;\n"
"    padding-bottom: 20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Microphone_page)
        QtCore.QMetaObject.connectSlotsByName(Microphone_page)

    def retranslateUi(self, Microphone_page):
        _translate = QtCore.QCoreApplication.translate
        Microphone_page.setWindowTitle(_translate("Microphone_page", "Form"))
        self.Label_head.setText(_translate("Microphone_page", "Microphone"))
        self.noise_button.setText(_translate("Microphone_page", "\n"
"detecting the sound coming into the headset, and generating signals \n"
"that are  out-of-phase with the  offending signals, canceling them out."))
        self.label.setText(_translate("Microphone_page", "Noise Suppression"))
        self.label_2.setText(_translate("Microphone_page", "Graph"))
        self.pushButton.setText(_translate("Microphone_page", "Test Microphone"))
