#!/usr/bin/python3
"""
Module 4-from_json_string
Contain a function that return an object (python data structure)
"""
import json


def from_json_string(my_str):
    """return an object(python data structure) represented by a JSON string"""
    return json.loads(my_str)
