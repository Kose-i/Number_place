#! /usr/bin/env python3

import sys

#from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
  app2 = QApplication(sys.argv)
  app = QApplication(sys.argv)
  
  your_window = QWidget()
  your_window.resize(450, 600)
  your_window.setWindowTitle("your_window")

  your_window.show()

  app.exec()
  app2.exec()
