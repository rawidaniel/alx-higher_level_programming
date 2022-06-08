#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for k, v in sorted(a_dictionary.items()):
            print(f"{k} : {v}")
    return None
