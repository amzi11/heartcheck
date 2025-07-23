from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

class SecondWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.lbl_name = QLabel(txt_name)
        self.inpt_name = QLineEdit()
        self.inpt_name.setPlaceholderText(txt_hintname)
        self.lbl_age = QLabel(txt_name)
        self.inpt_age = QLineEdit()
        self.inpt_age.setPlaceholderText(txt_hintage)

        self.lbl_test1 = QLabel(txt_test1)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.inpt_pulse1 = QLineEdit()
        self.inpt_pulse1.setPlaceholderText(txt_hinttest1)
        self.inpt_pulse1.setDisabled(True)


    def next_click(self):
        pass

    def connects(self):
        pass

    
    def set_appear(self):
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
