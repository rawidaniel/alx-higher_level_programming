#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string[:]
    if my_string is not None:
        for i in range(0, len(new_str)):
            if new_str[i] == "c" or new_str[i] == "C":
                new_str = new_str[0:i] + new_str[i + 1:]
                return new_str
