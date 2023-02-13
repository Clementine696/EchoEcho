#Microphone page TODO: guitar

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 670)
        MainWindow.setMinimumSize(QtCore.QSize(900, 670))
        MainWindow.setMaximumSize(QtCore.QSize(900, 670))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(62, 143, 156, 255), stop:1 rgba(74, 111, 117, 255));\n"
"border-style : outset;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(50, 110, 801, 181))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setTabletTracking(False)
        self.pushButton.setToolTip("")
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: #244D54;\n"
"    border-style : outset;\n"
"    border-width : 0.5px;\n"
"    border-top-left-radius : 40px;\n"
"    border-bottom-left-radius : 40px;\n"
"    border-top-right-radius : 40px;\n"
"    border-bottom-right-radius : 40px;\n"
"    border-color : black;\n"
"\n"
"    color: rgb(104, 104, 104);\n"
"    text-align : left;\n"
"    padding-left : 60;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(53, 112, 122);\n"
"\n"
"    border-width : 0.5px;\n"
"    border-color :  rgb(1, 209, 158) ;\n"
"    color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 20, 401, 71))
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 540, 801, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #244D54;\n"
"    border-style : outset;\n"
"    border-width : 0.5px;\n"
"    border-radius : 20px;\n"
"    border-color : black;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    text-align : left;\n"
"    padding-left:50;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-width : 0.5px;\n"
"    border-color :  rgb(1, 209, 158) ;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 110, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"color: rgb(204, 204, 204);\n"
"}")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 550, 21, 71))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 550, 21, 71))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 550, 21, 71))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 550, 21, 71))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 550, 21, 71))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 550, 21, 71))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(550, 550, 21, 71))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(580, 550, 21, 71))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(610, 550, 21, 71))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(640, 550, 21, 71))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(670, 550, 21, 71))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(700, 550, 21, 71))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(730, 550, 21, 71))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(760, 550, 21, 71))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(790, 550, 21, 71))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"    background-color: #D9D9D9;\n"
"    border-top-left-radius : 10px;\n"
"    border-top-right-radius : 10px;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-bottom-right-radius : 10px;\n"
"}")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 320, 801, 191))
        self.textBrowser.setStyleSheet("    background-color: #e5e5e5;\n"
"    border-style : outset;\n"
"    border-width : 0.5px;\n"
"    border-top-left-radius : 40px;\n"
"    border-bottom-left-radius : 40px;\n"
"    border-top-right-radius : 40px;\n"
"    border-bottom-right-radius : 40px;")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "\n"
"detecting the sound coming into the headset, and generating signals \n"
"that are  out-of-phase with the  offending signals, canceling them out."))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#ffffff;\">Microphone Mode</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Test Microphone"))
        self.label.setText(_translate("MainWindow", "Noise Suppression"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())