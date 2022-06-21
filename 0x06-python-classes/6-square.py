#!/usr/bin/python3
"Define a class Square"""


class Square:
    """Initialize a data,check the type of the size and
        raise TypeError if it is not and check the value of
        the size to be greater or equals to zero or raise
        ValueError if it is not. check the type of tuple and
        elements of the tuple either it is integer or grater than zero
        and raise TypeError if it is not.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    """Retrieve and update data"""
    @property
    def size(self):
        return self.__size
    """Retrieve and update data"""
    @property
    def position(self):
        return self.__position
    """Set the property's value"""
    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """Set the property's value"""
    @size.setter
    def size(self, value):
        if len(value) != 2 or value[0] < 0 or value[1] < 0 or \
           type(value) is not tuple or type(value[0]) is not int or \
           type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    """Calculate the area of the square."""
    def area(self):
        return self.size * self.size
    """prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
