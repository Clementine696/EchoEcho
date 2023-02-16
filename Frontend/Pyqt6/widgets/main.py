import sys
from PySide6 import *
from PyQt5.QtWidgets import QApplication, QMainWindow

# IMPORT GUI FILE
from ui_main import *
from soundpad_page import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_main()
        self.ui.setupUi(self)

        #Page links33
        ########################################################################################
        # Page Micrphone
        self.ui.Microphone_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Microphone_page))

        # Page Audio
        self.ui.Audio_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Audio_page))

        # Page Soundpad
        self.ui.Soundpad_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Soundpad_page))

        # Page Voice Changer
        self.ui.Voicechanger_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Voicechanger_page))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    nextGui = MainWindow()
    nextGui.show()
    sys.exit(app.exec_())
