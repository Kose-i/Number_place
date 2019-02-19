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

  enemy_window = QWidget()
  enemy_window.resize(300, 300)
  enemy_window.setWindowTitle("enemy_window")

  button_box =[]
  def change_title(i=0, j=0):
    button_box[i*9+j].setText('1')

  for i in range(0, 9):
    for j in range(0,9):
      button_box.append(QPushButton("", your_window))
      button_box[i*9 +j].setGeometry(50*i, 50*j, 50, 50)
      button_box[i*9 +j].clicked.connect(change_title(i,j))

  your_window.show()
  enemy_window.show()

  app.exec_()
