#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    i = len(my_list)
    for j in range(i):
        if my_list[j] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
