#! /usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton

class Base:
  def __init__(self, title, size_list = (450,600)):
    self.app = QApplication(sys.argv)
    self._window = QWidget()
    self._window.setWindowTitle(title)
    self._window.resize(size_list[0], size_list[1])
  def run(self):
    self._window.show()
  def __del__(self):
    self.app.exec_()

if __name__=='__main__':
  num = WindowNumberPlace("hehe", (250, 300))
  num.run()
