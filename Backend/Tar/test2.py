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

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton("Add", self)
        self.button.clicked.connect(lambda: self.add_file(""))
        self.progress_dialog = None

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.scroll_area)

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
                    
                  
                    self.table.setCellWidget(row, 2, self.play_button("Play", fname))

                    remove_button = self.remove_button(row, fname)
                    self.table.setCellWidget(row, 3, remove_button)
                    remove_button.clicked.connect(lambda _, r=row, f=fname: self.remove_file(r, f))
                
                print("audio load successfully")

        except Exception as e:
            print("Error loading audio files:",e)

    def add_file(self, file_path):
        options = QFileDialog.Options()
        folder = r""
        # เห็นเฉพาะ .wav, .mp3
        fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", folder, "WAV Files (*.wav);; MP3 Files (*.mp3)", options=options)

        if fname:
            print("add file :", fname)

            row = self.table.rowCount()
            self.table.insertRow(row)
            media_content = QMediaContent(QUrl.fromLocalFile(fname))
            self.player.setMedia(media_content)
            self.player.setNotifyInterval(1000)  
            content = QMediaContent(QUrl.fromLocalFile(fname))
            player = QMediaPlayer()
            player.setMedia(content)
            duration_label = QLabel(self)
            duration_label.setAlignment(QtCore.Qt.AlignRight)
            player.durationChanged.connect(lambda duration: self.update_duration(duration, duration_label))

            self.table.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))

            self.table.setCellWidget(row, 1, duration_label)
            
            self.table.setCellWidget(row, 2, self.play_button("Play", fname))

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

    def play_media(self, btn, fname):
        media_content = QMediaContent(QUrl.fromLocalFile(fname))
        if self.player.state() == QMediaPlayer.PlayingState and self.player.media().canonicalUrl() == media_content.canonicalUrl():
            self.player.stop()
            btn.setText("Play")
        else:
            self.player.setMedia(media_content)
            self.player.play()
            btn.setText("Stop")

    def update_duration(self, duration, duration_label):
    # Find the row corresponding to the given filename and update the duration item
        # for row in range(self.table.rowCount()):
        #     if self.table.item(row, 0).text() == os.path.basename(fname):
        #         duration_td = datetime.timedelta(milliseconds=duration)
        #         duration_str = duration_td.strftime("%M:%S")
        #         duration_label = self.table.cellWidget(row, 1)
        #         duration_label.setText(str(duration_td))
        duration_td = datetime.timedelta(milliseconds=duration)
        duration_str = str(duration_td)[2:]  # Remove the leading '0:'
        duration_label.setText(duration_str)

    def format_time(self, ms):
    # Convert milliseconds to minutes:seconds
        return datetime.timedelta(milliseconds=ms)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())