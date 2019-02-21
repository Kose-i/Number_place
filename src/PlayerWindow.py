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

class Change_button:
    def __init__(self,button_class, x, y):
        self.cls = button_class
        self.x = x
        self.y = y
    def __call__(self):
        PlayerWindow.set_button_text(self.cls, self.x, self.y)


class Check_number():
    def __init__(self, button_class, number):
        self.cls = button_class
        self.number = number
    def __call__(self):
        PlayerWindow.set_button_number(self.cls, self.number)

class Check_confirm_button:
    def __init__(self, button_class):
        self.cls = button_class
    def __call__(self):
        PlayerWindow.set_button_confirm(self.cls)


class PlayerWindow(window_numpla.Base):

    def __init__(self):
        print("__init__Player")
        super(PlayerWindow, self).__init__("Player-board", pos=(0, 0), size=(450, 600))

#INFO button_box
        self.button_box = [[QPushButton("", self._window) for i in range(0,9)] for j in range(0,9)]
        for i, list_line in enumerate(self.button_box):
            for j, list_elem in enumerate(list_line):
                list_elem.setGeometry(50*i, 50*j, 50, 50)
                list_elem.clicked.connect(Change_button(self, j,i))

#INFO output_messagebox - pos -
        self.output_messagebox = QLineEdit(self._window)
        self.output_messagebox.setText("[x]:0 [y]:0")
        self.output_messagebox.setGeometry(20, 470, 70, 20)
        self.output_messagebox.setReadOnly(True)

#INFO output_timer_messagebox - timer -
        self.output_timer_messagebox = QLineEdit(self._window)
        self.output_timer_messagebox.setText("Start!")
        self.output_timer_messagebox.setGeometry(110, 470, 150, 20)
        self.output_timer_messagebox.setReadOnly(True)

#INFO player_icon
        self.label = QLabel(self._window)
        self.player_icon = QIcon('img/PlayerImg.jpg')
        self.label.setPixmap(self.player_icon.pixmap(100, 100))
        self.label.setGeometry(300, 450, 100, 100)

#INFO number_button1~9+del
        self.number_button = [QPushButton("", self._window) for i in range(0,10)]
        for i, list_elem in enumerate(self.number_button):
            list_elem.setGeometry(20+20*i, 350+20*j, 20, 20)
            list_elem.clicked.connect(Check_number(self,i))
            if i == 0:
                self.number_button[i].setText("del")
            else:
                self.number_button[i].setText(str(i))

#INFO finish_button
        self.finish_button = QPushButton("", self._window)
        self.finish_button.setGeometry(220, 490, 70, 20)
        self.finish_button.setText("Finish")
        #self.finish_button.clicked.connect(self.set_finish())

#INFO confirm_button
        self.confirm_button = QPushButton("", self._window)
        self.confirm_button.setGeometry(220, 510, 70, 20)
        self.confirm_button.setText("Confirm")
        self.confirm_button.clicked.connect(Check_confirm_button(self))

#INFO input_messagebox
        self.input_messagebox = QLineEdit(self._window)
        self.input_messagebox.setText("")
        self.input_messagebox.setGeometry(20, 540, 410, 40)

#INFO __data_cell
        self.__data_cell = [[DataCell() for i in range(0, 9)] for j in range(0, 9)]
#INFO __last_y_pos, __last_x_pos
        self.__last_y_pos = 0
        self.__last_x_pos = 0

#INFO __is_not_access
        self.__is_not_access = [[False for i in range(0,9)] for j in range(0, 9)] # True from problem

#INFO __is_confirm
        self.__is_confirm = False


    def set_problem(self, problem):
        for  i, list_line in enumerate(self.button_box):
            for j, list_elem in enumerate(list_line):
                list_elem = problem[i][j]
                if problem[i][j] != 0:
                    self.__is_not_access[i][j] = True
                    self.__data_cell[i][j].num = problem[i][j]
                    self.button_box[i][j].setText(str(self.__data_cell[i][j].num))

    def run(self):
        super(PlayerWindow, self).run()

    def loose(self):
        self.label.setPixmap(self.player_icon.pixmap(80, 80, QIcon.Disabled))

    def set_button_text(self, x_pos, y_pos):
        self.button_box[self.__last_y_pos][self.__last_x_pos].setStyleSheet("background-color: white")
        self.button_box[y_pos][x_pos].setStyleSheet("background-color: red")
        self.output_messagebox.setText("[x]:"+str(x_pos)+" [y]:"+str(y_pos))
        self.__data_cell[self.__last_y_pos][self.__last_x_pos].string = str(self.input_messagebox.text())
        self.input_messagebox.setText(self.__data_cell[y_pos][x_pos].string)
        self.__last_y_pos = y_pos
        self.__last_x_pos = x_pos

    def set_button_number(self, number):
        if  self.__is_not_access[self.__last_y_pos][self.__last_x_pos] == True:
            return
        self.__data_cell[self.__last_y_pos][self.__last_x_pos].num = number
        display_text = str(self.__data_cell[self.__last_y_pos][self.__last_x_pos].num) if self.__data_cell[self.__last_y_pos][self.__last_x_pos].num > 0 else ""
        self.button_box[self.__last_y_pos][self.__last_x_pos].setText(display_text)

    def set_button_confirm(self):
        if self.__is_confirm == False:
            self.__is_confirm = True
            for  i, list_line in enumerate(self.button_box):
                for j, list_elem in enumerate(list_line):
                    if  self.__is_not_access[i][j] == True:
                        list_elem.setStyleSheet("background-color: white")
                    else:
                        list_elem.setStyleSheet("background-color: green")
        else:
            for  i, list_line in enumerate(self.button_box):
                for j, list_elem in enumerate(list_line):
                    list_elem.setStyleSheet("background-color: white")

    def set_finish(self):
        print(super(PlayerWindow, self).is_finish())
    
    def __del__(self):
        super(PlayerWindow, self).__del__()
        print("del__Player")


if __name__=='__main__':
    player = PlayerWindow()
    player.run()
