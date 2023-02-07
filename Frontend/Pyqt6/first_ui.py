import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 343)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Title"))

app = QtWidgets.QApplication(sys.argv) #จอเด้ง
win = QtWidgets.QMainWindow()

champ = Ui_Form() # oop เรียก บรรทัดนี้ก็ได้แล้ว
champ.setupUi(win)

win.show()
app.exec()

def main():
    app = QApplication(sys.argv)  # จอเด้ง
    win = Ui_Form()

    interface_UI = Ui_Form()  # oop เรียก บรรทัดนี้ก็ได้แล้ว
    interface_UI.setupUi(win)

    win.show()
    sys.exit(app.exec_())

main()
