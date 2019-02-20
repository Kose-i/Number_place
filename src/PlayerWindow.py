#! /usr/bin/env python3

from PyQt5.QtWidgets import QPushButton

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
        super(PlayerWindow, self).__init__("Player-board")

        self.__button_box = [[QPushButton("", self._window) for i in range(0,9)] for j in range(0,9)]
#TODO use enumerate
        for i in range(0, 9):
            for j in range(0,9):
                self.__button_box[i][j].setGeometry(50*i, 50*j, 50, 50)
                self.__button_box[i][j].clicked.connect(Change_button(self, j,i))

    def run(self):
        super(PlayerWindow, self).run()

    def set_button_text(self, x_pos, y_pos):
        self.__button_box[y_pos][x_pos].setText('1')
    
    def __del__(self):
        print("__del__Player")
        super(PlayerWindow, self).__del__()

if __name__=='__main__':
    player = PlayerWindow()
    player.run()
