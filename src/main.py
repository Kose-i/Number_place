#!/usr/bin/env python3

import time
import sys

import PlayerWindow
import ProblemChangeList as probtolist
import Computer

def main():
    pass

if __name__=='__main__':
    main()
    prob_str = ""
    if len(sys.argv) == 2:
      prob_str = sys.argv[1]
    else:
      prob_str = "../problem/problem5.txt"

    player = PlayerWindow.PlayerWindow()
    enemy = Computer.Computer()
    problem = probtolist.prob_to_list(prob_str)
    player.set_problem(problem)
    enemy.set_problem(problem)
    player.run()
    enemy.run()
