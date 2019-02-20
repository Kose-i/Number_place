#!/usr/bin/env python3

import time

import EnemyWindow
import PlayerWindow
import ProblemChangeList as probtolist

if __name__=='__main__':
    player = PlayerWindow.PlayerWindow()
    enemy = EnemyWindow.EnemyWindow()
    problem = probtolist.prob_to_list("../problem/problem1.txt")
    player.set_problem(problem)
    player.run()
    enemy.run()
