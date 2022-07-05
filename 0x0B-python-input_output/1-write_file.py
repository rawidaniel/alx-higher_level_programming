#!/usr/bin/python3

"""
Module 1-write_file
Contain a function that write a string to a text file
Return the number of character written
"""


def write_file(filename="", text=""):
    """write a string to a text file and return the number of chararcter"""
    with open(filename, 'w') as file_name:
        file_name.write(text)
    return len(text)
