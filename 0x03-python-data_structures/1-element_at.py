#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0 or idx > len(my_list):
        return None
    while i != idx:
        i += 1
    return my_list[i]
