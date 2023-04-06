import sys
import os
import shutil
import pickle
import time
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QDesktopWidget, QFileDialog,
    QTableWidget, QTableWidgetItem, QLabel, QMainWindow, QFormLayout,
    QGroupBox, QScrollArea, QVBoxLayout, QHBoxLayout, QProgressDialog, QLineEdit, QShortcut
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import QUrl
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

class App(QWidget):
    def __init__(self):

        super().__init__()

        self.filenames = []
        # self.hotkeys = {}
        self.count = [0] * len(self.filenames)
        self.player = QMediaPlayer()
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Filename", "Duration", "Play", "Remove", "count"])
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
                filenames_counts = pickle.load(file)
                for fname, count in filenames_counts:
                    row = self.table.rowCount()
                    self.table.insertRow(row)
                
                    self.table.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))
                
                    duration = self.getDuration(fname)
                    self.table.setItem(row, 1, QTableWidgetItem(duration))
                
                    self.table.setCellWidget(row, 2, self.play_button("Play", fname))
                
                    remove_button = self.remove_button(row, fname)
                    self.table.setCellWidget(row, 3, remove_button)
                    remove_button.clicked.connect(lambda _, r=row, f=fname: self.remove_file(r, f))
            
                    play_count = self.get_current_counts(fname)
                    self.table.setItem(row, 4, QTableWidgetItem(str(play_count)))

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
            self.table.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))

            duration = self.getDuration(fname)
            self.table.setItem(row, 1, QTableWidgetItem(duration))
            
            self.table.setCellWidget(row, 2, self.play_button("Play", fname))

            remove_button = QPushButton("Remove")
            remove_button.clicked.connect(lambda _, row=row, fname=fname: self.remove_file(row, fname))
            self.table.setCellWidget(row, 3, remove_button)

            play_count = QTableWidgetItem("0")
            self.table.setItem(row, 4, play_count)

            self.filenames.append(fname)
            self.save_file()

    def save_file(self):
        # save file in pickle
        print("save")
        with open("soundpad.pickle", "wb") as file:
        # convert the counts list to a tuple with the filename
            # filenames_counts = [(fname, self.get_current_counts(fname)) for fname in self.filenames]
            # pickle.dump(filenames_counts, file)
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
        # Stop currently playing song before playing new song
            if self.player.state() == QMediaPlayer.PlayingState:
                curr_fname = self.player.currentMedia().canonicalUrl().toLocalFile()
                curr_btn = self.get_play_button_by_fname(curr_fname)
                curr_btn.setText("Play")
                self.player.stop()

            self.player.setMedia(media_content)
            self.player.play()
            # self.get_current_counts()
            current_count = int(self.table.item(self.table.currentRow(), 4).text())
            current_count = current_count + 1
            self.table.item(self.table.currentRow(), 4).setText(str(current_count))
            # self.count.append(fname)
            # self.count[self.filenames.index(fname)] += 1
            # row = self.filenames.index(fname)
            # self.table.item(row, 4).setText(str(self.count[row]))

            # print(fname, current_count)

            self.player.setMedia(media_content)
            self.player.play()
            btn.setText("Stop")
        
        self.save_file()
    
    # def get_current_counts(self, fname):
    #     count = self.count[self.filenames.index(fname)] if fname in self.filenames else 0
    #     return count

    # def get_play_button_by_fname(self, fname):
    #     for row in range(self.table.rowCount()):
    #         if self.table.item(row, 0).text() == os.path.basename(fname):
    #             return self.table.cellWidget(row, 2)
        
    def getDuration(self, fname):
        if fname.endswith('.mp3'):
            audio = MP3(fname)
            duration = audio.info.length
        elif fname.endswith('.wav'):
            audio = WAVE(fname)
            duration = audio.info.length
        return time.strftime('%H:%M:%S', time.gmtime(duration))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())