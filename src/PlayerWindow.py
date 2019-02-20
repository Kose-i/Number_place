#! /usr/bin/env python3

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui     import QPixmap
from PyQt5.QtGui     import QIcon

import WindowNumberPlace as window_numpla

class DataCell:
    def __init__(self):
        self.string = "" 
        self.num = 0

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
        self.__input_messagebox.setGeometry(20, 560, 200, 30)

        self.__output_messagebox = QLineEdit(self._window)
        self.__output_messagebox.setText("[x]:0 [y]:0")
        self.__output_messagebox.setGeometry(20, 470, 100, 30)
        self.__output_messagebox.setReadOnly(True)

        self.__data_cell = [[DataCell() for i in range(0, 9)] for j in range(0, 9)]

        self.__button_box = [[QPushButton("", self._window) for i in range(0,9)] for j in range(0,9)]
        for i, list_line in enumerate(self.__button_box):
            for j, list_elem in enumerate(list_line):
                list_elem.setGeometry(50*i, 50*j, 50, 50)
                list_elem.clicked.connect(Change_button(self, j,i))
        self.__last_y_pos = 0
        self.__last_x_pos = 0

#XXX ?これはクラス内変数にする意味があるか
        self.label = QLabel(self._window)
        self.qicon = QIcon('img/PlayerImg.jpg')
        self.label.setPixmap(self.qicon.pixmap(80, 80))
        #label.setPixmap(qicon.pixmap(80, 80, QIcon.Disabled))
        self.label.setGeometry(300, 500, 80, 80)

        self.__is_not_access = [[False for i in range(0,9)] for j in range(0, 9)]

    def set_problem(self, *problem):
        for  i, list_line in enumerate(self.__button_box):
            for j, list_elem in enumerate(list_line):
                list_elem = problem[i][j]
                if problem[i][j] != 0:
                    self.__is_not_access[i][j] = True

    def run(self):
        super(PlayerWindow, self).run()

    def loose(self):
        self.label.setPixmap(self.qicon.pixmap(80, 80, QIcon.Disabled))

    def set_button_text(self, x_pos, y_pos):
        self.__output_messagebox.setText("[x]:"+str(x_pos)+" [y]:"+str(y_pos))
        self.__data_cell[self.__last_y_pos][self.__last_x_pos].string = self.__input_messagebox.text()
        self.__last_y_pos = y_pos
        self.__last_x_pos = x_pos
        if  self.__is_not_access[x_pos][y_pos] == True:
            return
        self.__data_cell[y_pos][x_pos].num += 1
        if  self.__data_cell[y_pos][x_pos].num > 9:
            self.__data_cell[y_pos][x_pos].num -= 10
        display_text = str(self.__data_cell[y_pos][x_pos].num) if self.__data_cell[y_pos][x_pos].num > 0 else ""
        self.__button_box[y_pos][x_pos].setText(display_text)
        self.__input_messagebox.setText(self.__data_cell[y_pos][x_pos].string)
    
    def __del__(self):
        super(PlayerWindow, self).__del__()
        print("del__Player")


if __name__=='__main__':
    player = PlayerWindow()
    player.run()
