#! /usr/bin/env python3

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

import WindowNumberPlace as window_numpla

class Change_button():
    def __init__(self,button_class, x, y):
        self.cls = button_class
        self.x = x
        self.y = y
    def __call__(self):
        PlayerWindow.set_button_text(self.cls, self.x, self.y)


class PlayerWindow(window_numpla.Base):

    def __init__(self):
        print("__init__Player")
        super(PlayerWindow, self).__init__("Player-board", pos=(0, 0), size=(450, 600))

        self.__input_messagebox = QLineEdit(self._window)
        self.__input_messagebox.setText("")
        self.__input_messagebox.displayText()
        self.__input_messagebox.setGeometry(30, 500, 200, 50)

        self.__button_box = [[QPushButton("", self._window) for i in range(0,9)] for j in range(0,9)]
        for i, list_line in enumerate(self.__button_box):
            for j, list_elem in enumerate(list_line):
                list_elem.setGeometry(50*i, 50*j, 50, 50)
                list_elem.clicked.connect(Change_button(self, j,i))

    def run(self):
        super(PlayerWindow, self).run()

    def set_button_text(self, x_pos, y_pos):
        self.__button_box[y_pos][x_pos].setText('1')
    
    def __del__(self):
        super(PlayerWindow, self).__del__()
        print("del__Player")


if __name__=='__main__':
    player = PlayerWindow()
    player.run()
