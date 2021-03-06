#! /usr/bin/env python3

def prob_to_list(file_name):
    ans_list = [[0 for i in range(0,9)] for j in range(0,9)]
    with open(file_name, 'r') as f:
        str_box = f.readlines()
    for i in range(0,9):
        for j in range(0,9):
            ans_list[i][j] = int(str_box[i][j])
    return ans_list

if __name__=='__main__':
    lists = prob_to_list("../problem/prob_1.txt")
    for i, lists_line in enumerate(lists):
        print(lists_line)
