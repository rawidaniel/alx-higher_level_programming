#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = my_list[:]
        new_list[search - 1] = replace
        return new_list
    return None
