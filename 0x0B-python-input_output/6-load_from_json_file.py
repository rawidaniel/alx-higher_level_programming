#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contain a function create an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """create an object from a JSON file"""
    with open(filename, 'r') as file_name:
        return json.load(file_name)
