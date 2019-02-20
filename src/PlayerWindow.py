#! /usr/bin/env python3

import WindowNumberPlace as window_numpla

class PlayerWindow(window_numpla.Base):
  def __init__(self):
    print("__init__Player")
    super(PlayerWindow, self).__init__("Player-board")
  def run(self):
#    self.__window.
    super(PlayerWindow, self).run()
  def __del__(self):
    print("__del__Player")
    super(PlayerWindow, self).__del__()

if __name__=='__main__':
  player = PlayerWindow()
  player.run()
