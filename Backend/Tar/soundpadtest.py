import sys
import os
import shutil
import pickle
import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QDesktopWidget, QFileDialog,
    QTableWidget, QTableWidgetItem, QLabel, QMainWindow, QFormLayout,
    QGroupBox, QScrollArea, QVBoxLayout, QHBoxLayout, QProgressDialog
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import QUrl

class App(QWidget):
    def __init__(self):

        super().__init__()

        self.filenames = []
        self.player = QMediaPlayer()
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Filename", "Duration", "Play", "Remove"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.cellClicked.connect(self.play_button)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.table)
        self.scroll_area.setWidgetResizable(True)

        self.title = 'EchoEcho'
        self.left = 200
        self.top = 100
        self.width = 1280
        self.height = 720
        self.initUI()
        # self.load_file()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton("Add", self)
        self.button.clicked.connect(lambda: self.add_file(""))
        self.progress_dialog = None

        # self.remove_button = QPushButton("Remove", self)
        # # self.remove_button.clicked.connect(self.remove_file)
        # self.remove_button.clicked.connect(self.remove_file)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.scroll_area)
        # layout.addWidget(self.remove_button)

        self.setLayout(layout)

        self.load_file()

    def load_file(self):
        # read file in pickle
        try:
            with open("soundpad.pickle", "rb") as file:
                self.filenames = pickle.load(file)
                for fname in self.filenames:
                    row = self.table.rowCount()
                    self.table.insertRow(row)
                    self.table.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))
                    self.table.setItem(row, 1, QTableWidgetItem(""))
                    # self.get_duration(QMediaPlayer.LoadedMedia, fname, row)
                    self.table.setCellWidget(row, 2, self.play_button("Play", fname))
                    # remove_button = QPushButton("Remove")
                    # remove_button.clicked.connect(lambda _, row=row, fname=fname: self.remove_file(row, fname))
                    # self.table.setCellWidget(row, 3, remove_button)
                    remove_button = self.remove_button(row, fname)
                    self.table.setCellWidget(row, 3, remove_button)
                    remove_button.clicked.connect(lambda _, r=row, f=fname: self.remove_file(r, f))
                print("audio load successfully")

        except Exception as e:
            print("Error loading audio files:",e)

    def add_file(self, file_path):
        options = QFileDialog.Options()
        folder = r""
        # เห็นทุกไฟล์    
        # fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", folder, "All Files (*)", options=options)

        # เห็นเฉพาะ .wav, .mp3
        fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", folder, "WAV Files (*.wav);; MP3 Files (*.mp3)", options=options)
        # print("add file :", fname)

        # row = self.table.rowCount()
        # self.table.insertRow(row)
        # self.table.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))
        # self.table.setItem(row, 1, QTableWidgetItem(""))
        # self.get_duration(QMediaPlayer.LoadedMedia, fname, row)
        # self.table.setCellWidget(row, 2, self.play_button("Play", fname))
        # remove_button = QPushButton("Remove")
        # remove_button.clicked.connect(lambda _, row=row, fname=fname: self.remove_file(row, fname))
        # self.table.setCellWidget(row, 3, remove_button)
        # self.filenames.append(fname)
        # self.save_file()

        if fname:
            print("add file :", fname)

            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))
            # self.table.setItem(row, 1, QTableWidgetItem(""))
            # self.get_duration(QMediaPlayer.LoadedMedia, fname, row)
            media_content = QMediaContent(QUrl.fromLocalFile(fname))
            self.player.setMedia(media_content)
            self.player.setNotifyInterval(1000)
            # self.get_duration(lambda: self.get_duration(fname, row))
            # self.get_duration(fname, row)
            # self.table.setItem(row, 1, QTableWidgetItem("Loading..."))  
            content = QMediaContent(QUrl.fromLocalFile(fname))
            player = QMediaPlayer()
            player.setMedia(content)
            player.durationChanged.connect(lambda duration: self.setDuration(row, duration))
            player.error.connect(lambda error: self.handleError(row, error))
            status = QTableWidgetItem("Loading...")
            self.table.setItem(row, 1, status)
       
            # self.table.setCellWidget(row, 2, self.play_button("Play", fname))
            self.table.setCellWidget(row, 2, self.play_button(row, fname, player))
            remove_button = QPushButton("Remove")
            remove_button.clicked.connect(lambda _, row=row, fname=fname: self.remove_file(row, fname))
            self.table.setCellWidget(row, 3, remove_button)
            self.filenames.append(fname)
            self.save_file()

    def save_file(self):
        # save file in pickle
        with open("soundpad.pickle", "wb") as file:
            pickle.dump(self.filenames, file)

    def remove_button(self, row, fname):
        button = QPushButton("Remove")
        button.clicked.connect(lambda: self.remove_file(row, fname))
        return button

    def remove_file(self, row, fname):
        # Remove the selected row from the table
        if fname in self.filenames:
            self.filenames.remove(fname)
        self.table.removeRow(row)
        # os.remove() 

        # self.filenames.remove(fname)
        # self.table.removeRow(row)

        # Save the updated list of filenames
        self.save_file()

        # Stop the player if it was playing the removed file
        if self.player.state() == QMediaPlayer.PlayingState and self.player.currentMedia().canonicalUrl().toLocalFile() == fname:
            self.player.stop()

        print("File removed successfully.")

    def play_button(self, label, fname):
        button = QPushButton(label)
        button.clicked.connect(lambda: self.play_media(button, fname))
        return button

    # def play_media(self, filename, row):
    #     fname = filename
    #     # convert string to QUrl object using the QUrl constructor
    #     file = QUrl.fromLocalFile(fname)
    #     media = QMediaContent(file)
    #     self.player.setMedia(media)
    #     # play the media
    #     # self.player.play()
    #     if self.player.state() == QMediaPlayer.PausedState:
    #         self.player.play()
    #     else:
    #         self.player.pause()

    def play_media(self, btn, fname):
        media_content = QMediaContent(QUrl.fromLocalFile(fname))
        if self.player.state() == QMediaPlayer.PlayingState and self.player.media().canonicalUrl() == media_content.canonicalUrl():
            self.player.stop()
            btn.setText("Play")
        else:
            self.player.setMedia(media_content)
            self.player.play()
            btn.setText("Stop")

        #Kod jeng loey nong Yah
        
    # def get_duration(self, fname, row, status):
    # #     # duration = self.player.duration() / 1000.0
    # #     # self.table.setItem(row, 1, QTableWidgetItem("{:.2f} s".format(duration)))
    # #     duration = self.player.duration()
    # #     if duration >= 0:
    # #         duration = str(datetime.timedelta(milliseconds=duration))
    # #         self.table.setItem(row, 1, QTableWidgetItem(duration))
    # #     else:
    # #         QtCore.QTimer.singleShot(1000, lambda: self.get_duration(fname, row))
    #      if status == QMediaPlayer.LoadedMedia:
    #         duration = self.player.duration() // 1000
    #         self.table.setItem(row, 1, QTableWidgetItem(str(datetime.timedelta(seconds=duration))))
    #         self.progress_dialog.close()

    def setDuration(self, row, duration):
        durationItem = QTableWidgetItem(f"{duration/1000:.2f} s")
        self.setItem(row, 1, durationItem)
        
    def handleError(self, row, error):
        status = QTableWidgetItem("Error")
        self.setItem(row, 2, status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())