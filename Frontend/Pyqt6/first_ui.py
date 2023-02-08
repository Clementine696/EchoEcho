# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

win = QMainWindow()

btn = QPushButton('My button')


def calledBtn(a):
    print(a)
btn.clicked.connect(calledBtn)


win.setCentralWidget(btn)
win.show()

app.exec()
