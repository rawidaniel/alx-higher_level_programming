#!/usr/bin/python3
"""
Module 0-read_file
Contain method that read a text file and print to stdout
"""


def read_file(filename=""):
    """read from tetx file and print to stdout"""
    with open(filename, 'r') as file:
        print(file.read().strip('\n'))
