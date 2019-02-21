#!/usr/bin/env python3

import time

import PlayerWindow
import ProblemChangeList as probtolist
import ComputerEasy

def main():
    pass

if __name__=='__main__':
    main()
    player = PlayerWindow.PlayerWindow()
    enemy = ComputerEasy.ComputerEasy()
    problem = probtolist.prob_to_list("../problem/confirm1.txt")
    player.set_problem(problem)
    enemy.set_problem(problem)
    player.run()
    enemy.run()
