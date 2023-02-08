import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QListWidget

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.filenames = []
        self.list = QListWidget(self)

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
        self.button.clicked.connect(self.add_sound)

    def add_sound(self):
        # 
        options = QFileDialog.Options()

        # เห็นแค่ไฟล์ mp3, mp4, wav
        # fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "MP3 Files (*.mp3);; MP4 Files (*.mp4);; WAV Files (*.wav)", options=options)
        
        # เห็นทุกไฟล์
        fname, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)", options=options)

        if fname:
        # Put files in list
            self.filenames.append(fname)
        # Display list in UI
            self.list.addItem(fname)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())