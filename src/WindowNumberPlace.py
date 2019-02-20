#! /usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication,QWidget
#from PyQt5.QtWidgets import QPushButton

class Base:
    count = 0
    def __init__(self, title, pos = (0, 0), size = (450,600)):
        if Base.count == 0:
            Base.app = QApplication(sys.argv)
        Base.count += 1
        self._window = QWidget()
        self._window.setWindowTitle(title)
        self._window.setGeometry(pos[0], pos[1], size[0], size[1])

    def run(self):
        self._window.show()

    def __del__(self):
        Base.count -= 1
        if Base.count == 0:
            self.app.exec()

    def is_finish(self):
        pass

if __name__=='__main__':
    num = Base("hehe", (250, 300))
    num.run()
