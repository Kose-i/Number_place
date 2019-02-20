#! /usr/bin/env python3

import sys

#from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton

if __name__=='__main__':
  app = QApplication(sys.argv)
  
  your_window = QWidget()
  your_window.resize(450, 600)
  your_window.setWindowTitle("your_window")

#  enemy_window = QWidget()
#  enemy_window.resize(300, 300)
#  enemy_window.setWindowTitle("enemy_window")

  button_box = [[QPushButton("", your_window) for i in range(0,9)] for j in range(0,9)]

  for i in range(0, 9):
    for j in range(0,9):
      button_box[i][j].setGeometry(50*i, 50*j, 50, 50)

  class Change_button:
    def __init__(self, i, j):
      self.x = i
      self.y = j
    def __call__(self):
      button_box[self.x][self.y].setText('1')

  for i in range(0, 9):
    for j in range(0,9):
      button_box[i][j].clicked.connect(Change_button(i,j))

  your_window.show()
#  enemy_window.show()

  app.exec_()
