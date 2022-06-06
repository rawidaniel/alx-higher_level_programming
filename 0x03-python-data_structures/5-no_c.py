#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    i = 0
    if my_string is not None:
        while i < length:
            if my_string[i] == "c" or my_string[i] == "C":
                my_string = my_string[0:i] + my_string[i + 1:]
                length -= 1
            i += 1
    return my_string
