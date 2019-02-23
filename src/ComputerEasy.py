#! /usr/bin/env python3

import EnemyWindow
import ProblemChangeList as probtolist

class ComputerEasy(EnemyWindow.EnemyWindow):
    def __init__(self):
        super(ComputerEasy, self).__init__()
        self.__cell_list = [[[[0] for i in range(0,9)] for j in range(0,9)] for k in range(0,9)]

    def first_step(self):
        for i in range(0,9):
            for j in range(0,9):
                for k in range(0,9):
                    self.__cell_list[i][j][k] = k + 1
        for i in range(0,9):
            for j in range(0,9):
                if self.get_can_access(i, j) == False :
                    for l in range(0,9):
                        if self.cell_num[j][i] != l+1:
                            print(self.cell_num[j][i])
                            self.__cell_list[i][j].remove(l+1)
        self.print_cell_list()

    def print_cell_list(self):
        for i in range(0,9):
            for j in range(0,9):
                print(self.__cell_list[i][j])

    def run(self):
        self.first_step()


if __name__=='__main__':
    enemy = ComputerEasy()
    problem = probtolist.prob_to_list("../problem/problem1.txt")
    enemy.set_problem(problem)
    enemy.run()
