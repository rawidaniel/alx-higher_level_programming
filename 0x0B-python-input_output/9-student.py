#!/usr/bin/python3
"""
Module 9-student

Contain class student with public method to_json
"""


class Student:
    """
    Class that represent student

    Parameter
    ---------
    first_name : str
        First name of student
    last_name : str
        Last name of student
    age : int
        The age of the student

    Method
    -----------
    to_josn
        retrieves a dictionary representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """instantiate first_name, last_name and age attributes

        Parameter
        ---------
        first_name : str
            First name of student
        last_name : str
            Last name of student
        age : int
            The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Return
        --------
        dict
            dictionary representation of a Student instance
        """
        return self.__dict__
