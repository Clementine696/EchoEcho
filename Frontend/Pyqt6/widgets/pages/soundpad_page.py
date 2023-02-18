from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Soundpad(object):
    def setupUi(self, Soundpad_F):
        Soundpad_F.setObjectName("Soundpad_F")
        Soundpad_F.resize(900, 680)
        Soundpad_F.setMinimumSize(QtCore.QSize(900, 680))
        Soundpad_F.setMaximumSize(QtCore.QSize(900, 680))
        Soundpad_F.setStyleSheet("\n"
                                 "\n"
                                 "background-color: rgb(36, 77, 84);\n"
                                 "")
        self.verticalLayout = QtWidgets.QVBoxLayout(Soundpad_F)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.body = QtWidgets.QFrame(Soundpad_F)
        self.body.setMaximumSize(QtCore.QSize(900, 680))
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")

        # Title Frame
        self.SP_title = QtWidgets.QFrame(self.body)
        self.SP_title.setGeometry(QtCore.QRect(1, 0, 900, 120))
        self.SP_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_title.setObjectName("SP_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SP_title)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.SP_title)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Title label
        self.SP_title_label = QtWidgets.QLabel(self.frame)
        self.SP_title_label.setGeometry(QtCore.QRect(0, 0, 900, 120))
        self.SP_title_label.setMinimumSize(QtCore.QSize(900, 120))
        self.SP_title_label.setMaximumSize(QtCore.QSize(900, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.SP_title_label.setFont(font)
        self.SP_title_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.SP_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SP_title_label.setObjectName("SP_title_label")

        # Table Frame
        self.verticalLayout_2.addWidget(self.frame)
        self.SP_table = QtWidgets.QFrame(self.body)
        self.SP_table.setGeometry(QtCore.QRect(0, 130, 900, 560))
        self.SP_table.setMaximumSize(QtCore.QSize(900, 680))
        self.SP_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SP_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SP_table.setObjectName("SP_table")
        self.verticalLayout.addWidget(self.body)

        # Table
        self.SP_tabel_widget = QtWidgets.QWidget(self.SP_table)
        self.SP_tabel_widget.setGeometry(QtCore.QRect(0, 0, 900, 560))
        self.SP_tabel_widget.setMinimumSize(QtCore.QSize(900, 560))
        self.SP_tabel_widget.setMaximumSize(QtCore.QSize(900, 560))
        self.filenames = []
        # self.player = QMediaPlayer()
        self.SP_tabel_widget = QTableWidget()
        self.SP_tabel_widget.setColumnCount(3)
        self.SP_tabel_widget.setHorizontalHeaderLabels(
            ["Filename", "Duration", "Action"])
        self.SP_tabel_widget.horizontalHeader().setStretchLastSection(True)
        # self.SP_tabel_widget.cellClicked.connect(self.create_button_widget)

        self.retranslateUi(Soundpad_F)
        QtCore.QMetaObject.connectSlotsByName(Soundpad_F)

    def retranslateUi(self, Soundpad_F):
        _translate = QtCore.QCoreApplication.translate
        Soundpad_F.setWindowTitle(_translate("Soundpad_F", "Form"))
        self.SP_title_label.setText(_translate("Soundpad_F", "Soundpad"))