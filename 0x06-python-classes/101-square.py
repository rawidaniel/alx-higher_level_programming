#!/usr/bin/python3
"Define a class Square"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a data,check the type of the size and
        raise TypeError if it is not and check the value of
        the size to be greater or equals to zero or raise
        ValueError if it is not. check the type of tuple and
        elements of the tuple either it is integer or grater than zero
        and raise TypeError if it is not.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve and update data"""
        return self.__size

    @property
    def position(self):
        """Retrieve and update data"""
        return self.__position

    @size.setter
    def size(self, value):
        """Set the property's value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Set the property's value"""
        if len(value) != 2 or value[0] < 0 or value[1] < 0 or \
           type(value) is not tuple or type(value[0]) is not int or \
           type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return (self.__size) ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(["#" * self.__size if self.__position[1] > 0 else
                            " " * self.__position[0] + "#" * self.__size
                             for rows in range(self.__size)]))

    def __str__(self):
        """String representation of square class instance."""
        string = ""
        if self.__size == 0:
            return string
        else:
            string += "\n" * self.__position[1]
            string += "\n".join([" " * self.__position[0] + "#" * self.__size
                                 for i in range(self.__size)])
            return string
