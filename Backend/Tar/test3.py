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

        # self.filenames = []
        # # self.hotkeys = {}
        # self.count = []
        self.data = []
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
        # options = QFileDialog.Options()
        # folder = r""
      
        # เห็นเฉพาะ .wav, .mp3
        # fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '.', 'Pickle files(*.pickle)')
        
        # read file in pickle
        try:
            with open("soundpad.pickle", "rb") as file:
                data = pickle.load(file)
            self.table.setRowCount(len(data))
                # self.filenames = pickle.load(file)
            for row, item in enumerate(data):
                fname = QTableWidgetItem(item[0])
                play_count = QTableWidgetItem(str(item[1]))

                row = self.table.rowCount()
                self.table.insertRow(row)
                    
                self.table.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))
                    
                duration = self.getDuration(fname)
                self.table.setItem(row, 1, QTableWidgetItem(duration))

                self.table.setCellWidget(row, 2, self.play_button("Play", fname))

                remove_button = self.remove_button(row, fname)
                self.table.setCellWidget(row, 3, remove_button)
                remove_button.clicked.connect(lambda _, r=row, f=fname: self.remove_file(r, f))
                
                self.table.setItem(row, 4, play_count)

                self.data.append((fname, int(play_count.text())))

            print("audio load successfully")

        except Exception as e:
            print("Error loading audio files:", e)

    def add_file(self, file_path):
        options = QFileDialog.Options()
        folder = r""

        # เห็นเฉพาะ .wav, .mp3
        fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", folder, "WAV Files (*.wav);; MP3 Files (*.mp3)", options=options)
        if fname:
            print("add file :", fname)

            row = self.table.rowCount()
            self.table.setRowCount(row + 1)
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(os.path.basename(fname)))

            duration = self.getDuration(fname)
            self.table.setItem(row, 1, QTableWidgetItem(duration))

            self.table.setCellWidget(row, 2, self.play_button("Play", fname))

            remove_button = QPushButton("Remove")
            remove_button.clicked.connect(lambda _, row=row, fname=fname: self.remove_file(row, fname))
            self.table.setCellWidget(row, 3, remove_button)

            play_count_item = QTableWidgetItem('0')
            self.table.setItem(row, 4, play_count_item)

            # self.filenames.append(fname)
            self.save_file()

    def save_file(self):
        # save file in pickle
        # options = QFileDialog.Options()
        # folder = r""

        # fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", folder, "WAV Files (*.wav);; MP3 Files (*.mp3)", options=options)
        data = []
        
        for row in range(self.table.rowCount()):
            fname = self.table.item(row, 0)
            play_count = int(self.table.item(row, 4).text())
            data.append([fname, play_count])
        with open("soundpad.pickle", "wb") as file:
            pickle.dump(data, file)

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

            # self.player.setMedia(media_content)
            # self.player.play()
            # btn.setText("...")
            # current_count = int(self.table.item(self.table.currnteRow(), 4).text())
            # self.table.item(self.table.currentRow(), 4).setText(str(current_count + 1))

            self.player.setMedia(media_content)
            self.player.play()
            btn.setText("Stop")

    def get_play_button_by_fname(self, fname):
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).text() == os.path.basename(fname):
                return self.table.cellWidget(row, 2)

    def update_play_count(self):
        row = self.table.currentRow()
        column = self.table.currentColumn()

        if column == 1:
            play_count_item = self.table.item(row, column)
            play_count = int(play_count_item.text()) + 1
            play_count_item.setText(str(play_count))
        
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