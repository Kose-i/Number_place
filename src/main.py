#!/usr/bin/env python3

import time
import sys
import threading

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
      prob_str = "../problem/problem2.txt"

    player = PlayerWindow.PlayerWindow()
    enemy = Computer.Computer()
    problem = probtolist.prob_to_list(prob_str)
    player.set_problem(problem)
    enemy.set_problem(problem)
    thread1 = threading.Thread(target=player.run)
    thread2 = threading.Thread(target=enemy.run)
    thread1.start()
    thread2.start()
