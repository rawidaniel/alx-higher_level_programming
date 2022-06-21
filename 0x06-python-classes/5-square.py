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
    """Retrieve and update data"""
    @property
    def size(self):
        return self.__size
    """Set the property's value"""
    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    """Calculate the area of the square."""
    def area(self):
        return self.size * self.size
    """prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n".join(["#" * self.__size for i in range(self.__size)]))
