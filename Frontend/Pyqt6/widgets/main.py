import sys
from PySide6 import *
from PyQt5.QtWidgets import QApplication

# IMPORT GUI FILE
from interface import *

# MAIN WINDOW CLASS

def main():
    app = QApplication(sys.argv)
    win = Ui_interface()

    win.show()
    sys.exit(app.exec_())

main()
