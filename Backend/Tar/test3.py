import sys
import os
import glob
import time
from PyQt5.QtCore import QUrl, Qt, QFile, QIODevice, QTextStream, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.loadFiles()

        app = QApplication.instance()
        app.aboutToQuit.connect(self.saveFiles)

    def initUI(self):
        self.setWindowTitle('Audio File Recorder')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)

        self.add_file_button = QPushButton('Add File')
        self.add_file_button.clicked.connect(self.addFile)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['File Name', 'Duration', 'Play', 'Delete'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.central_layout.addWidget(self.add_file_button, 0, 0)
        self.central_layout.addWidget(self.table, 1, 0)

        self.setCentralWidget(self.central_widget)

    def addFile(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter('Audio Files (*.wav *.mp3)')
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_names = []
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_names = file_dialog.selectedFiles()
            for file_name in file_names:
                if os.path.splitext(file_name)[1] in ('.wav', '.mp3'):
                    duration = self.getDuration(file_name)

                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    self.table.setItem(row_position, 0, QTableWidgetItem(os.path.basename(file_name)))
                    self.table.setItem(row_position, 1, QTableWidgetItem(duration))

                    player = QMediaPlayer()
                    content = QMediaContent(QUrl.fromLocalFile(file_name))
                    player.setMedia(content)

                    play_button = QPushButton('Play')
                    play_button.setObjectName(file_name)
                    play_button.clicked.connect(lambda _, b=file_name, p=player: self.playAudio(b, p))
                    self.table.setCellWidget(row_position, 2, play_button)

                    delete_button = QPushButton('Delete')
                    delete_button.clicked.connect(lambda state, row=row_position: self.deleteFile(row))
                    self.table.setCellWidget(row_position, 3, delete_button)

                    self.saveFiles()

    def loadFiles(self):
        try:
            with open('soundpad.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    file_name, duration = line.strip().split(',')
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    self.table.setItem(row_position, 0, QTableWidgetItem(os.path.basename(file_name)))
                    self.table.setItem(row_position, 1, QTableWidgetItem(duration))

                    player = QMediaPlayer()
                    content = QMediaContent(QUrl.fromLocalFile(file_name))
                    player.setMedia(content)

                    play_button = QPushButton('Play')
                    play_button.setObjectName(file_name)
                    play_button.clicked.connect(lambda _, b=file_name, p=player: self.playAudio(b, p))
                    self.table.setCellWidget(row_position, 2, play_button)

                    delete_button = QPushButton('Delete')
                    delete_button.clicked.connect(lambda state, row=row_position: self.deleteFile(row))
                    self.table.setCellWidget(row_position, 3, delete_button)

                print("audio load successfully")

        except Exception as e:
            print("Error loading audio files:",e)

    def deleteFile(self, row):
        self.table.removeRow(row)

        with open('soundpad.txt', 'r') as f:
            lines = f.readlines()
        with open('soundpad.txt', 'w') as f:
            for i, line in enumerate(lines):
                if i != row:
                    f.write(line)
        
    def playAudio(self, file_name, player):
        if  player.mediaStatus() == QMediaPlayer.LoadedMedia:
            player.stop()

        content = QMediaContent(QUrl.fromLocalFile(file_name))
        player.setMedia(content)
        player.play()

    def getDuration(self, file_name):
        if file_name.endswith('.mp3'):
            audio = MP3(file_name)
            duration = audio.info.length
        elif file_name.endswith('.wav'):
            audio = WAVE(file_name)
            duration = audio.info.length
        return time.strftime('%H:%M:%S', time.gmtime(duration))
    
    def saveFiles(self):
        with open('soundpad.txt', 'w') as f:
            for row in range(self.table.rowCount()):
                file_name = self.table.item(row, 0).text()
                duration = self.table.item(row, 1).text()
                f.write(f"{file_name},{duration}\n")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())