#!/usr/bin/env python3

import time

import EnemyWindow
import PlayerWindow

if __name__=='__main__':
    player = PlayerWindow.PlayerWindow()
    time.sleep(1)
    enemy = EnemyWindow.EnemyWindow()
    player.run()
    enemy.run()
