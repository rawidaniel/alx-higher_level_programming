#!/usr/bin/python3
"""
Module 0-read_file
Contain function that read a text file and print to stdout
"""


def read_file(filename=""):
    """read from tetx file and print to stdout"""
    with open(filename, mode='r', encoding="utf-8") as file_name:
        print(file_name.read(), end="")
