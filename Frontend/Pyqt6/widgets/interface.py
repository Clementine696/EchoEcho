import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_interface(QMainWindow):
    def __init__(self):
        super(Ui_interface, self).__init__()
        self.setObjectName("Form")
        self.setEnabled(True)
        self.resize(1280, 720)
        self.setMinimumSize(QtCore.QSize(1280, 720))
        self.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        # font.setFamily("Segoe UI")
        # font.setPointSize(12)
        # Form.setFont(font)
        self.setMouseTracking(False)
        self.setAutoFillBackground(False)
        
        #Left Side
        self.Left_side = QtWidgets.QFrame(self)
        self.Left_side.setGeometry(QtCore.QRect(10, 10, 380, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Left_side.sizePolicy().hasHeightForWidth())
        self.Left_side.setSizePolicy(sizePolicy)
        self.Left_side.setMinimumSize(QtCore.QSize(380, 700))
        self.Left_side.setMaximumSize(QtCore.QSize(380, 700))
        self.Left_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Left_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Left_side.setObjectName("Left_side")
        
        # MenuBars
        self.Menubars = QtWidgets.QFrame(self.Left_side)
        self.Menubars.setGeometry(QtCore.QRect(10, 10, 360, 330))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menubars.sizePolicy().hasHeightForWidth())
        self.Menubars.setSizePolicy(sizePolicy)
        self.Menubars.setMinimumSize(QtCore.QSize(360, 330))
        self.Menubars.setMaximumSize(QtCore.QSize(360, 330))
        self.Menubars.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menubars.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menubars.setObjectName("Menubars")
        
        # Device Settings
        self.Device_settings = QtWidgets.QFrame(self.Left_side)
        self.Device_settings.setGeometry(QtCore.QRect(10, 360, 360, 330))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Device_settings.sizePolicy().hasHeightForWidth())
        self.Device_settings.setSizePolicy(sizePolicy)
        self.Device_settings.setMinimumSize(QtCore.QSize(360, 330))
        self.Device_settings.setMaximumSize(QtCore.QSize(360, 330))
        self.Device_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Device_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Device_settings.setObjectName("Device_settings")
        
        # Right Side
        self.Right_side = QtWidgets.QFrame(self)
        self.Right_side.setGeometry(QtCore.QRect(400, 10, 870, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Right_side.sizePolicy().hasHeightForWidth())
        self.Right_side.setSizePolicy(sizePolicy)
        self.Right_side.setMinimumSize(QtCore.QSize(800, 700))
        self.Right_side.setMaximumSize(QtCore.QSize(870, 700))
        self.Right_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Right_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Right_side.setObjectName("Right_side")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # self.setupUI()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EchoEcho"))