# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *
from second_win import SecondWin
class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.lbl_hello = QLabel(txt_hello)
        self.lbl_instr = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)

        self.layout_main = QVBoxLayout()
        self.layout_main.addWidget(self.lbl_hello, alignment = Qt.AlignLeft)
        self.layout_main.addWidget(self.lbl_instr, alignment = Qt.AlignLeft)
        self.layout_main.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_main)

    def next_click(self):
        self.hide()
        self.sw = SecondWin()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click) 
 
    def set_appear(self):
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)

app = QApplication([])
mw = MainWin()
app.exec_()