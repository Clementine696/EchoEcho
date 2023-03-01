import sys
import os
import shutil
import pickle
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QFileDialog, QListWidget, QListWidgetItem, QLabel, QMainWindow, QFormLayout, QGroupBox, QScrollArea, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import QUrl

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.filenames = []
        self.player = QMediaPlayer()
        self.list = QListWidget()
        self.list.itemClicked.connect(self.play_media)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.list)
        self.scroll_area.setWidgetResizable(True)

        self.title = 'EchoEcho'
        self.left = 200
        self.top = 100
        self.width = 1280
        self.height = 720
        self.initUI()
        self.load_file()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.button = QPushButton("Add", self)
        self.button.clicked.connect(self.add_file)

        self.remove_button = QPushButton("Remove", self)
        self.remove_button.clicked.connect(self.remove_file)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

        layout.addWidget(self.scroll_area)
        layout.addWidget(self.remove_button)
        
        self.setLayout(layout)

    def load_file(self):

        # read file in pickle
        try:
            with open("filenames.pickle", "rb") as file:
                self.filenames = pickle.load(file)
                for fname in self.filenames:
                    self.list.addItem(fname)
                    print("audio load successfully")
        except Exception as e:  
            print(e)  

    def add_file(self, file_path):
        
        options = QFileDialog.Options()
        folder = r""
        # เห็นทุกไฟล์    
        fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", folder, "All Files (*)", options=options)
        print("add file :", fname)

        item = QListWidgetItem(fname)
        self.list.addItem(item)
        self.filenames.append(fname)
        self.save_file()

    def save_file(self):

        # save file in pickle
        with open("filenames.pickle", "wb") as file:
            pickle.dump(self.filenames, file)

    def remove_file(self):
        
        selected = self.list.selectedItems()

        # ลบไฟล์ที่เลือกออกจาก list
        for item in selected:
            row = self.list.row(item)
            self.list.takeItem(row)
            removed_file = self.filenames.pop(row)
        # read file in pickle
            with open("filenames.pickle", "rb") as file:
                filenames = pickle.load(file)
        # remove file
                filenames.remove(removed_file)
        # write pickle
            with open("filenames.pickle", "wb") as file:
                pickle.dump(filenames, file)

    def play_media(self, item):

        fname = item.text()
        # convert string to QUrl object using the QUrl constructor
        file = QUrl.fromLocalFile(fname)
        media = QMediaContent(file)
        self.player.setMedia(media)
        # play the media
        self.player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())