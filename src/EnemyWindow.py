#! /usr/bin/env python3

from PyQt5.QtWidgets import QPushButton

import WindowNumberPlace as window_numpla

class EnemyWindow(window_numpla.Base):

    def __init__(self):
        print("__init__Enemy")
        super(EnemyWindow, self).__init__("Enemy-board", (270,300))

        self.__button_box = [[QPushButton("", self._window) for i in range(0,9)] for j in range(0,9)]
#TODO use enumerate
        for i in range(0, 9):
            for j in range(0,9):
                self.__button_box[i][j].setGeometry(30*i, 30*j, 30, 30)

    def run(self):
        super(EnemyWindow, self).run()

    def set_button_text(self, x_pos, y_pos, number):
        self.__button_box[y_pos][x_pos].setText(number)
    
    def __del__(self):
        print("__del__Enemy")
        super(EnemyWindow, self).__del__()

if __name__=='__main__':
    player = EnemyWindow()
    player.run()
