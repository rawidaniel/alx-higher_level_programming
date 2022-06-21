#!/usr/bin/python3
"Define a class Square"""


class Square:
    """Initialize a data,check the type of the size and
        raise TypeError if it is not and check the value of
        the size to be greater or equals to zero or raise
        ValueError if it is not.
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
    """Calculate the area of the square."""
    def area(self):
        return self.__size * self.__size
