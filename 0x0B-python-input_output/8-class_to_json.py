#!/usr/bin/python3
"""
Module 8-class_t0_json

Contain function class_to_json
Returns dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure

    Parameter
    ---------
    obj : object
        The instance of the class

    Return
    --------
    dictionary
        dictionary description of the object
    """
    return obj.__dict__
