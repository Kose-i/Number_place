#! /usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton

class WindowNumberPlace:
  def __init__(self, title, size_list = (450,600)):
    self.app = QApplication(sys.argv)
    self.__window = QWidget()
    self.__window.setWindowTitle(title)
    self.__window.resize(size_list[0], size_list[1])
  def run(self):
    self.__window.show()
  def __del__(self):
    self.app.exec_()

if __name__=='__main__':
  num = WindowNumberPlace("hehe")
  num.run()
