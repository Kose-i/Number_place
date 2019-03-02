#! /usr/bin/env python3

import copy

import EnemyWindow
import ProblemChangeList as probtolist

class Computer(EnemyWindow.EnemyWindow):
    def __init__(self):
        super(Computer, self).__init__()
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

    @staticmethod
    def del_line_cell_list(lists, target_num, line_num, row_num):
        for i in range(0,9):
            if row_num != i and lists[line_num][i].count(target_num) > 0:
                lists[line_num][i].remove(target_num)

    @staticmethod
    def del_row_cell_list(lists, target_num, line_num, row_num):
        for i in range(0,9):
            if line_num != i and lists[i][row_num].count(target_num) > 0:
                lists[i][row_num].remove(target_num)

    @staticmethod
    def del_block_cell_list(lists, target_num, line_num, row_num):
        block_line =3*( line_num // 3)
        block_row = 3*(row_num // 3)
        for i in range(0,3):
            for j in range(0,3):
                if lists[block_line+i][block_row+j].count(target_num) > 0:
                    if line_num == block_line +i and row_num == block_row +j:
                        pass
                    else:
                        lists[block_line+i][block_row+j].remove(target_num)

    def update_first_step(self):
        for i in range(0,9):
            for j in range(0,9):
                if len(self.__cell_list[i][j]) == 1:
                    Computer.del_row_cell_list(self.__cell_list, self.__cell_list[i][j][0], i, j)
                    Computer.del_line_cell_list(self.__cell_list, self.__cell_list[i][j][0], i, j)
                    Computer.del_block_cell_list(self.__cell_list, self.__cell_list[i][j][0], i, j)

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
        for i, list_line in enumerate(self.__cell_list):
            for j, list_elem in enumerate(list_line):
                if len(list_elem) == 1:
                    self.set_button_number(i, j, list_elem[0])
                    self.__now_open += 1

    def print_cell_list(self):
        for i in range(0,9):
            for j in range(0,9):
                print(self.__cell_list[i][j])

    def first_run(self):
        self.first_step()
        tmp_open = 0
        for i in range(0,10):
            self.update_first_step()
            self.update_button_print()
            self.update_second_step()
            if tmp_open == self.__now_open:
                break
            tmp_open = self.__now_open
        if self.__now_open == 81:
            self.finish()

    @staticmethod
    def del_update_cell(lists):
        for i in range(0,9):
            for j in range(0,9):
                if len(lists[i][j]) == 1:
                    Computer.del_row_cell_list(lists, lists[i][j][0], i, j)
                    Computer.del_line_cell_list(lists, lists[i][j][0], i, j)
                    Computer.del_block_cell_list(lists, lists[i][j][0], i, j)

    def is_ok_update(self, lists):
        for i, cell_line in enumerate(lists):
            for j, elem in enumerate(cell_line):
                if self.get_can_access(i,j) == True and len(elem) == 0:
                    return False
        return True

    def is_finish_update(self, lists):
        for i, cell_line in enumerate(lists):
            for j, cell_elem in enumerate(cell_line):
                if self.get_can_access(j, i) == True and len(cell_elem) != 1:
                    return False
        return True

    def second_run_update(self, lists):
        Computer.del_update_cell(lists)
        if self.is_ok_update(lists) == False:
            return [], False
        if self.is_finish_update(lists) == True:
            return lists, True
        for i, line_lists in enumerate(lists):
            for j, elem_lists in enumerate(line_lists):
                if len(elem_lists) != 1:
                    tmp_lists = copy.deepcopy(lists)
                    for k, elem in enumerate(elem_lists):
                        tmp = []
                        tmp.append(elem)
                        tmp_lists[i][j] = tmp
                        tmp_lists_update = []
                        tmp_lists_update, ok = self.second_run_update(tmp_lists)
                        if ok == True:
                            return tmp_lists_update, True
        return [], False

    def second_run(self):
        tmp_cell_list = copy.deepcopy(self.__cell_list)
        tmp_cell_list, ok = self.second_run_update(tmp_cell_list)
        if ok == True:
            self.__cell_list = tmp_cell_list
            self.finish()
        else:
            self.speak("Not answer")
        self.update_button_print()

    def finish(self):
        speakString = "I am finish. ranking:" + str(self.is_finish())
        self.speak(speakString)

    def run(self):
        self.first_run()
        if self.__now_open != 81:
            self.second_run()


#if __name__=='__main__':
#    enemy = Computer()
#    problem = probtolist.prob_to_list("../problem/problem1.txt")
#    enemy.set_problem(problem)
#    enemy.run()
