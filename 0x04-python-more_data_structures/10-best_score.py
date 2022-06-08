#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        biggest = 0
        big_key = ""
        for k, v in a_dictionary.items():
            if v > biggest:
                biggest = v
                big_key = k
        return big_key
    return None
