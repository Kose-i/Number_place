#! /usr/bin/env python3

import EnemyWindow
import ProblemChangeList as probtolist

class ComputerEasy(EnemyWindow.EnemyWindow):
    def __init__(self):
        super(ComputerEasy, self).__init__()
    def run(self):
        pass


if __name__=='__main__':
    enemy = ComputerEasy()
    problem = probtolist.prob_to_list("../problem/problem1.txt")
    enemy.set_problem(problem)
    enemy.run()
