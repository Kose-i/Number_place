#!/usr/bin/env python3

import time

import EnemyWindow
import PlayerWindow
import ProblemChangeList as probtolist
import ComputerEasy

if __name__=='__main__':
    player = PlayerWindow.PlayerWindow()
#    enemy = EnemyWindow.EnemyWindow()
    enemy = ComputerEasy.ComputerEasy()
    problem = probtolist.prob_to_list("../problem/problem1.txt")
    player.set_problem(problem)
    enemy.set_problem(problem)
    player.run()
    enemy.run()
