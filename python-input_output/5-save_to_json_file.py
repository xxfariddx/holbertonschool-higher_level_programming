#!/usr/bin/python3
"""
Module that contains a function to save an object to a file in JSON format
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
