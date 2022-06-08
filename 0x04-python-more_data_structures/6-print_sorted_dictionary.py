#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for k in sorted(a_dictionary):
            print(f"{k} :{a_dictionary[k]}")
    return None
