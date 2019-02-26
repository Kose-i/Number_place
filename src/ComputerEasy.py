#! /usr/bin/env python3

import EnemyWindow
import ProblemChangeList as probtolist

class ComputerEasy(EnemyWindow.EnemyWindow):
    def __init__(self):
        super(ComputerEasy, self).__init__()
        self.__cell_list = [[[[0] for i in range(0,9)] for j in range(0,9)] for k in range(0,9)]
        self.__now_open = 0

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
                            self.__cell_list[i][j].remove(l+1)

    def del_line_cell_list(self, target_num, line_num):
        for i in range(0,9):
            if len(self.__cell_list[line_num][i]) != 1 and self.__cell_list[line_num][i].count(target_num) != 0:
                self.__cell_list[line_num][i].remove(target_num)
    def del_row_cell_list(self, target_num, row_num):
        for i in range(0,9):
            if len(self.__cell_list[i][row_num]) != 1 and self.__cell_list[i][row_num].count(target_num) != 0:
                self.__cell_list[i][row_num].remove(target_num)
    def del_block_cell_list(self, target_num, line_num, row_num):
        block_line =3*( line_num // 3)
        block_row = 3*(row_num // 3)
        for i in range(0,3):
            for j in range(0,3):
                if len(self.__cell_list[block_line+i][block_row+j]) != 1 and self.__cell_list[block_line+i][block_row+j].count(target_num) != 0:
                    self.__cell_list[block_line+i][block_row+j].remove(target_num)

    def update_first_step(self):
        for i in range(0,9):
            for j in range(0,9):
                if len(self.__cell_list[i][j]) == 1:
                    self.del_row_cell_list(self.__cell_list[i][j][0], j)
                    self.del_line_cell_list(self.__cell_list[i][j][0], i)
                    self.del_block_cell_list(self.__cell_list[i][j][0], i, j)

    def set_row_cell_list(self, x_pos, y_pos, num):
        for i in range(0,9):
            if i != x_pos and self.__cell_list[i][y_pos].count(num) != 0:
                return
        tmp = []
        tmp.append(num)
        self.__cell_list[x_pos][y_pos] = tmp

    def set_line_cell_list(self, x_pos, y_pos, num):
        for i in range(0,9):
            if i != y_pos and self.__cell_list[x_pos][i].count(num) != 0:
                return
        tmp = []
        tmp.append(num)
        self.__cell_list[x_pos][y_pos] = tmp

    def set_block_cell_list(self, x_pos, y_pos, num):
        block_line =3*( x_pos // 3)
        block_row = 3*( y_pos // 3)
        for i in range(0,3):
            for j in range(0,3):
                if block_line+i == x_pos and block_row+j == y_pos:
                    continue
                if self.__cell_list[block_line+i][block_row+j].count(num) != 0:
                    return
        tmp = []
        tmp.append(num)
        self.__cell_list[x_pos][y_pos] = tmp

    def update_second_step(self):
        for i in range(0,9):
            for j in range(0,9):
                for k in range(1,10):
                    if len(self.__cell_list[i][j]) != 1 and self.__cell_list[i][j].count(k) != 0:
                        self.set_row_cell_list(i, j, k)
                        self.set_line_cell_list(i, j, k)
                        self.set_block_cell_list(i, j, k)

    def update_button_print(self):
        self.__now_open = 0
        for i in range(0,9):
            for j in range(0,9):
                if len(self.__cell_list[i][j]) == 1:
                    self.set_button_number(i, j, self.__cell_list[i][j][0])
                    self.__now_open += 1
        #print(self.__now_open)

    def print_cell_list(self):
        for i in range(0,9):
            for j in range(0,9):
                print(self.__cell_list[i][j])

    def run(self):
        self.first_step()
        for i in range(0,10):
          self.update_first_step()
          self.update_button_print()
          self.update_second_step()
          if self.__now_open == 81:
              speakString = "I am finish. ranking:" + str(self.is_finish())
              self.speak(speakString)
              break


if __name__=='__main__':
    enemy = ComputerEasy()
    problem = probtolist.prob_to_list("../problem/problem1.txt")
    enemy.set_problem(problem)
    enemy.run()
