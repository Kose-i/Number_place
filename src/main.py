#!/usr/bin/env python3

import PlayerWindow
import EnemyWindow

if __name__=='__main__':
    player = PlayerWindow.PlayerWindow()
    enemy = EnemyWindow.EnemyWindow()
    player.run()
    enemy.run()
