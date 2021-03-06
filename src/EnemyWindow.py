#! /usr/bin/env python3

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui     import QPixmap
from PyQt5.QtGui     import QIcon

import WindowNumberPlace as window_numpla

class EnemyWindow(window_numpla.Base):

    def __init__(self):
        print("__init__Enemy")
        super(EnemyWindow, self).__init__("Enemy-board", pos=(450, 0) , size=(270,320))

#INFO button_box
        self.button_box = [[QPushButton("", self._window) for i in range(0,9)] for j in range(0,9)]
        for i, list_line in enumerate(self.button_box):
            for j, list_elem in enumerate(list_line):
                list_elem.setGeometry(30*j, 30*i, 30, 30)

#INFO output_messagebox - talk -
        self.output_messagebox = QLineEdit(self._window)
        self.output_messagebox.setText("I am Enemy for you")
        self.output_messagebox.setGeometry(20, 280, 180, 30)
        self.output_messagebox.setReadOnly(True)
#INFO enemy_icon
        self.label = QLabel(self._window)
        self.player_icon = QIcon('img/EnemyImg.jpg')
        self.label.setPixmap(self.player_icon.pixmap(50, 50))
        self.label.setGeometry(210, 270, 50, 50)
        super(EnemyWindow, self).run()
#INFO __is_access -> getter -> access[i][j]
        self.__is_not_access = [[False for i in range(0,9)] for j in range(0, 9)] # True from problem
        self.cell_num = [[[0]for i in range(0,9)]for j in range(0,9)]

    def get_can_access(self, x_pos, y_pos):
        if self.__is_not_access[y_pos][x_pos] == True:
            return False
        else:
            return True

    def set_problem(self, problem):
        for  i, list_line in enumerate(self.button_box):
            for j, list_elem in enumerate(list_line):
                list_elem = problem[i][j]
                if problem[i][j] != 0:
                    self.__is_not_access[i][j] = True
                    self.cell_num[i][j] = problem[i][j]
#                    print(self.cell_num)
                    self.button_box[i][j].setText(str(self.cell_num[i][j]))

    def run(self):
        pass

    def speak(self, str):
        self.output_messagebox.setText(str)

    def set_button_number(self, x_pos, y_pos, number):
        self.button_box[y_pos][x_pos].setText(str(number))
    def del_button_number(self, x_pos, y_pos):
        self.button_box[y_pos][x_pos].setText("")
    
    def __del__(self):
        super(EnemyWindow, self).__del__()
        print("__del__Enemy")

if __name__=='__main__':
    enemy = EnemyWindow()
    #enemy.set_button_number(2,3,'3')
    enemy.run()
