from PyQt5.QtCore import Qt, QTimer, Qtime
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
        self.lbl_age = QLabel(txt_age)
        self.inpt_age = QLineEdit()
        self.inpt_age.setPlaceholderText(txt_hintage)

        self.lbl_test1 = QLabel(txt_test1)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.inpt_pulse1 = QLineEdit()
        self.inpt_pulse1.setPlaceholderText(txt_hinttest1)
        self.inpt_pulse1.setDisabled(True)

        self.lbl_instr2 = QLabel(txt_test2)
        self.btn_instr2 = QPushButton(txt_starttest2)
        self.btn_instr2.setDisabled(True)

        self.lbl_test2 = QLabel(txt_test3)
        self.btn_test2 = QPushButton(txt_starttest3)
        self.btn_test2.setDisabled(True)
        self.inpt_pulse2 = QLineEdit()
        self.inpt_pulse2.setPlaceholderText(txt_hintage)
        self.inpt_pulse2.setDisabled(True)
        self.inpt_pulse3 = QLineEdit()
        self.inpt_pulse3.setPlaceholderText(txt_hintage)
        self.inpt_pulse3.setDisabled(True)
        self.btn_result = QPushButton(txt_sendresults)
        self.btn_result.setDisabled(True)


        self.lbl_timer = QLabel(txt_timer)

        self.layout_v1 = QVBoxLayout()

        self.layout_v1.addWidget(self.lbl_name, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.inpt_name, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.lbl_age, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.inpt_age, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.lbl_test1, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.inpt_pulse1, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.lbl_instr2, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.btn_instr2, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.lbl_test2, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.inpt_pulse2, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.inpt_pulse3, alignment = Qt.AlignLeft)
        self.layout_v1.addWidget(self.btn_result, alignment = Qt.AlignCenter)
        
        
        self.layout_v2 = QVBoxLayout()
        self.layout_v2.addWidget(self.lbl_timer, alignment = Qt.AlignRight)

        self.layout_main = QHBoxLayout()
        self.layout_main.addLayout(self.layout_v1)
        self.layout_main.addLayout(self.layout_v2)

        self.setLayout(self.layout_main)
                 
    def next_click(self):
        pass

    def connects(self):
        pass

    
    def set_appear(self):
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
