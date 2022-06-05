#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string[:]
    length = len(my_string)
    i = 0
    if my_string is not None:
        while i < length:
            if new_str[i] == "c" or new_str[i] == "C":
                new_str = new_str[0:i] + new_str[i + 1:]
                length -= 1
            i += 1
        return new_str
